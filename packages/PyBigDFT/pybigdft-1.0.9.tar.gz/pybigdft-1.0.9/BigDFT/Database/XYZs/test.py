from pyscf import gto, dft
from sys import argv

mol = gto.Mole()
mol.atom = argv[2]
mol.basis = argv[1]
mol.verbose = 4
mol.build()
rks = dft.RKS(mol)
rks.xc = 'b97_1'
rks.kernel()
print(rks.e_tot)
