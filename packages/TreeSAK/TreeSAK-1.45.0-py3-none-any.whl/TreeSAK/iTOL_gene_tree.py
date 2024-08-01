import os
import argparse
from ete3 import Tree


iTOL_gene_tree_usage = '''
================== iTOL_gene_tree example commands ==================

TreeSAK -g gene.tree -i genome_taxon.txt -o gene_taxon.txt
TreeSAK -g gene.tree -i genome_habitat.txt -o gene_habitat.txt
TreeSAK -g gene.tree -i genome_abundance.txt -o gene_abundance.txt

=====================================================================
'''


def iTOL_gene_tree(args):

    tree_file = args['g']
    meta_txt  = args['i']
    op_txt    = args['o']

    if os.path.isfile(tree_file) is False:
        print('Tree file not found, program exited!')
        exit()

    if os.path.isfile(meta_txt) is False:
        print('Metadata file not found, program exited!')
        exit()

    metadata_dict = dict()
    for each_gnm in open(meta_txt):
        each_gnm_split = each_gnm.strip().split('\t')
        if len(each_gnm_split) == 2:
            gnm_id = each_gnm_split[0]
            meta_value = each_gnm_split[1]
            metadata_dict[gnm_id] = meta_value

    op_txt_handle = open(op_txt, 'w')
    for leaf in Tree(tree_file, format=1):
        leaf_name = leaf.name
        gnm_name  = '_'.join(leaf_name.split('_')[:-1])
        gnm_meta  = metadata_dict.get(gnm_name, 'na')
        op_txt_handle.write('%s\t%s\n' % (leaf_name, gnm_meta))
    op_txt_handle.close()

    print('Done!')


if __name__ == '__main__':

    iTOL_gene_tree_parser = argparse.ArgumentParser(usage=iTOL_gene_tree_usage)
    iTOL_gene_tree_parser.add_argument('-i',     required=True,     help='input metadata')
    iTOL_gene_tree_parser.add_argument('-g',     required=True,     help='gene tree file')
    iTOL_gene_tree_parser.add_argument('-o',     required=True,     help='output metadata')
    args = vars(iTOL_gene_tree_parser.parse_args())
    iTOL_gene_tree(args)
