#!/usr/bin/env python3

"""
Usage: ./scRNA.py
"""

import sys
import numpy as np
import scanpy.api as sc
import matplotlib
matplotlib.use("Agg")
sc.settings.autoshow = False

# Read 10x dataset
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
# Make variable names (in this case the genes) unique
adata.var_names_make_unique()

sc.tl.pca(adata)
sc.pl.pca(adata, save='unfiltered.png')

sc.pp.recipe_zheng17(adata)

sc.tl.pca(adata)
sc.pl.pca(adata, save='filtered.png')

sc.pp.neighbors(adata)
sc.tl.louvain(adata)
sc.tl.tsne(adata)
adata.rename_categories('louvain', ['0', 'interneurons1', '2', '3', '4', 'superficial CA1PC', '6', 'astrocytes', '8', 'deep CA1PC', 'oligodendrocytes', '11', '12', 'dopaminergic', 'interneurons2', '15', '16', 'interneurons3', '18', 'endothelial', '20', 'mural', 'microglia'])
sc.pl.tsne(adata, legend_loc='on data', color=('louvain', 'Gad1', 'Aldoc', 'Aif1', 'Hba-a2', 'Sox5', 'Cldn5', 'Dbi', 'Zbtb20', 'Nrxn3', 'Pdgfrb', 'Olig1'), save='labeled.png')
sc.tl.umap(adata)
sc.pl.umap(adata, color=('louvain', 'Gad1', 'Aldoc', 'Aif1', 'Hba-a2', 'Sox5', 'Cldn5', 'Dbi', 'Zbtb20', 'Nrxn3', 'Pdgfrb', 'Olig1'), save='labeled.png')
#
# sc.pl.dotplot(adata, ['Gapdh', 'Gad1', 'Gad2', 'Slc17a6', 'Slc17a7', 'Slc6a5', 'Cacna1a', 'Cacna1b'], save='dotplot.png')

# sc.tl.rank_genes_groups(adata, 'louvain', method='t-test')
# sc.pl.rank_genes_groups(adata, save='t-test.png')
#
# sc.tl.rank_genes_groups(adata, 'louvain', method='logreg')
# sc.pl.rank_genes_groups(adata, save='logreg.png')