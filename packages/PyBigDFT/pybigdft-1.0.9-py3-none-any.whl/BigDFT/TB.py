"""
This module enables to compute the electronic properties of a solid state 
system using the matrices produced by a linear scaling calculation in BigDFT
"""

###
# add periodicity to matching_index
# add args to shell_matrix for matchin_index tolerance
# add axis to plot_bs
###

AU_eV = 27.21138386


class TightBinding():
    """
    Defines the tight-binding object associated to 
        -a system (Systems.System)
        -an interaction radius (int)
    """
    from BigDFT.Systems import System

    def __init__(self, sys=System(), d=5):
        self.sys = sys
        self.BZ = self._BZ()
        self.R_sh = self._sites_in_shell(d)

    def _BZ(self):
        """
        Given a system, finds its Brillouin zone (BZ)
        """
        from numpy import cross, dot, where, roll, ones, round, inf, pi
        from copy import deepcopy

        a = deepcopy(self.sys.cell.cell)
        a[where(a == inf)] = 1e12
        V = dot(a[0], cross(a[1], a[2]))
        b = ones((3, 3))*2*pi/V

        idx = range(0, 3)
        for i in idx:
            i1, i2, i3 = roll(idx, -i)
            b[i1] *= cross(a[i2], a[i3])

        return {'cell': round(b, 12)}

    def _sites_in_shell(self, d):
        """
        Given a system, finds the pairs between atoms and their periodic images
        up to a specified distance, along with their Bravais vectors

        Args:
            sys (Systems.System): the periodic system
            d (float): the threshold distance

        Returns:
            R_sh (dict): a mapping between atom sites, their difference in
            cell index and Bravais vectors
        """
        from numpy import linalg, array, where, ceil

        cell = self.sys.cell.cell
        a1, a2, a3 = cell
        nx, ny, nz = ceil(d/linalg.norm(cell, axis=1)).astype(int)
        R_n, id_n = self.sys.cell.tiling_vectors([nx, ny, nz])

        R_sh = {}
        for i, ai in enumerate(self.sys.get_atoms()):
            ri = array(ai.get_position(units='angstroem'))
            for j, aj in enumerate(self.sys.get_atoms()):
                rj = array(aj.get_position(units='angstroem'))
                R_ij = (rj-ri)+array(R_n)
                d_ij = linalg.norm(R_ij, axis=1)
                iR, = where(d_ij < d)
                for ir, idk in zip(iR, array(id_n)[iR]):
                    R_sh.update({(i, j, tuple(idk)): list(R_ij[ir])})

        return R_sh

    def matching_index(self, sys_e, r0_e=None, tol=.1):
        """
        Given two systems, finds the atom indices where the minimal system 
        matches the extended one.

        Args:
            sys_e (Systems.System): the extended system
            r0_e (3d-array): the origin of self.sys in sys_e
            tol (float): tolerance for matching systems

        Returns:
            (dict): a mapping between the atom indices that maximise 
            the matching, with the associated error
        """
        from numpy import array, mean, argmin
        from scipy.spatial import distance_matrix

        pos_e = array([at.get_position(units='angstroem') 
                       for at in sys_e.get_atoms()])
        pos_s = array([at.get_position(units='angstroem') 
                       for at in self.sys.get_atoms()])
        if r0_e is None:
            r0_e = mean(pos_e, axis=0)
        dist = distance_matrix(pos_e, r0_e.reshape(1, 3))
        ir0_e = argmin(dist)

        dd = {}
        for i, ri in enumerate(pos_s):
            pos_i = pos_s - ri + pos_e[ir0_e]
            dist = distance_matrix(pos_e, pos_i)
            ii = argmin(dist, axis=0)
            di = sum(sum([(i-j)**2 for i, j in zip(pos_e[ii], pos_i)]))
            dd[i] = {'idx': list(ii), 'mse': di}

        ddi = {k: v['mse'] for k, v in dd.items()}
        idmin = min(ddi, key=ddi.get)
        if dd[idmin]['mse'] > tol:
            print('Warning: matching less than tolerance')

        return dd[idmin]

    def shell_matrix(self, sys_e, mat, metadata):
        """
        Given a mapping between atom sites and their periodic images, retrieves
        their matrices from a linear-scaling calculation. The correspondance 
        between the mapping and the run is given by a list of indices.

        Args:
            R_sh (dict): a mapping between atom sites and their periodic 
            images, their difference in cell index and positions vectors
            sys (Systems.System): the linear-scaling system
            mat (list): the sparse matrices, H and S (scipy.sparse.csc_matrix)
            metadata (Spillage.MatrixMetadata): the information on the matrices

        Returns
            H_sh (dict): a mapping between the atom sites, their difference in
            cell index and their hamiltonian matrix
            S_sh (dict): idem for overlap matrix
        """
        from numpy import array, argmin, meshgrid, cumsum
        from scipy.spatial import distance_matrix

        idx = self.matching_index(sys_e)['idx']
        id_mat = [metadata.atoms[i].get('indices') for i in idx]
        id_orb = cumsum([0]+[len(i) for i in id_mat])

        pos = array([at.get_position(units='angstroem') 
                     for at in sys_e.get_atoms()])
        h, s = [i.todense() for i in mat]

        H_sh, S_sh = {}, {}
        for (i, j, idk), R_ij in self.R_sh.items():
            r_j = array([pos[idx[i]] + R_ij])
            d_ij = distance_matrix(pos, r_j)
            idx_j = argmin(d_ij)
            idH_i = metadata.atoms[idx[i]].get('indices')
            idH_j = metadata.atoms[idx_j].get('indices')
            X, Y = meshgrid(idH_i, idH_j)
            h_ij, s_ij = h[X, Y], s[X, Y]
            H_sh.update({(i, j, idk): h_ij})
            S_sh.update({(i, j, idk): s_ij})

        return {'id': {'atoms': idx, 'orbs': list(id_orb)},
                'h': H_sh, 's': S_sh}

    def k_path(self, hsp, n=101):
        """
        Given a set of high-symmetry points, finds the corresponding k-path
        """
        from numpy import dot, zeros, linspace, concatenate

        b = self.BZ['cell']
        path = [dot(i, b) for i in hsp.values()]

        k = zeros((0, 3))
        for hs0, hs1 in zip(path[:-1], path[1:]):
            k = concatenate((k, linspace(hs0, hs1, n)))

        return k

    def k_matrix(self, k, m_sh): 
        """
        Given a mapping between atom sites and their perdiodic images, their 
        Bravais vectors and their matrix elements, this function computes
        the k-resolved matrices

        Args:
            k (array): the k-points sampling
            m_sh (list): a mapping between the atom sites and matrices
            idmat (list): orbitals number per atom

        Returns:
            The k-resolved matrices and energy spectrum
        """
        from numpy import array, zeros, meshgrid, dot, outer, exp, complex64

        id_orb = m_sh['id']['orbs']
        H_sh, S_sh = m_sh['h'], m_sh['s']

        Nk, No = len(k), id_orb[-1]
        Hk = zeros((Nk, No, No), dtype=complex64)
        Sk = zeros((Nk, No, No), dtype=complex64)

        for (i, j, idk), R_ij in self.R_sh.items():
            i0, i1 = id_orb[i], id_orb[i+1]
            j0, j1 = id_orb[j], id_orb[j+1]
            idm_i = [i0+ii for ii in range(i1-i0)]
            idm_j = [j0+jj for jj in range(j1-j0)] 
            X, Y = meshgrid(idm_i, idm_j)  # indexing
            li, lj = len(idm_i), len(idm_j)
            h_ij = H_sh[(i, j, idk)]
            s_ij = S_sh[(i, j, idk)]
            a = exp(-1j*dot(k, array(R_ij)))
            Hk[:, X, Y] += outer(a, h_ij).reshape(Nk, lj, li)
            Sk[:, X, Y] += outer(a, s_ij).reshape(Nk, lj, li)

        from scipy.linalg import eigh

        Ek = zeros(Hk.shape[:2])
        for ik in range(len(k)):
            try:
                w, v = eigh(Hk[ik], b=Sk[ik])
            except ValueError:
                print("Error at ik=", ik)
            Ek[ik, :] = w

        return Hk, Sk, Ek


def plot_bs(k, Ek, ax=None):
    """
    Given a k-path and its eigenvalues, plot the band structure
    """
    from numpy import linalg, concatenate, cumsum
    from matplotlib import pyplot as plt

    dk = linalg.norm(k[1:]-k[:-1], axis=1)
    kpath = concatenate(([0], cumsum(dk)))

    if ax is None:
        _, ax = plt.subplots(figsize=(3.2, 4.8))
    plt.plot(kpath, Ek*AU_eV, ms=.7)
    plt.xlim([0, kpath[-1]])
    plt.xticks([])
    plt.yticks(size=8)
    plt.ylabel('Energy (eV)', size=10)

    return ax
