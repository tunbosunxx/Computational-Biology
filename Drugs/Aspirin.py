from rdkit import Chem
from rdkit.Chem import AllChem

mol = Chem.MolFromSmiles('CC(=O)OC1=CC=CC=C1C(=O)O')
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, randomSeed=42)
AllChem.MMFFOptimizeMolecule(mol, maxIters=500, nonBondedThresh=500.0)
writer = Chem.SDWriter('Aspirin.sdf')
writer.write(mol)
writer.close()