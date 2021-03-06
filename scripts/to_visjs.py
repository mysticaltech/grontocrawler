#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# # Convert nx graph to JSON files
#
# Nodes and edges into respective JSON files for further re-use in other apps

"""
   Copyright 2015-2017 Asan Agibetov <asan.agibetov@gmail.com>

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import os
import sys


gronto_folder = os.path.dirname(os.path.abspath(__file__))
gronto_folder = os.path.join(gronto_folder, '..')
sys.path.insert(0, gronto_folder)

from rdflib import Graph

import argparse
from grontocrawler.io import to_visjs
from grontocrawler.graph import produce_graph
# CL tool to convert OWL ontology to Networkx graph and then to `visjs` graph format
#
def main():
    parser = argparse.ArgumentParser()

    def_input = os.path.join(gronto_folder, './shared/ontology/hypo_onto.owl')
    def_output_nodes = os.path.join(gronto_folder, './shared/visjs/nodes.json')
    def_output_arcs = os.path.join(gronto_folder, './shared/visjs/arcs.json')

    parser.add_argument('-i', '--input-ontology', default=def_input)
    parser.add_argument('-f', '--ontology-format', default='turtle')
    parser.add_argument('--output-nodes', default=def_output_nodes)
    parser.add_argument('--output-arcs', default=def_output_arcs)
    # rules for graph edge production
    parser.add_argument('--options', nargs='+', default=None)

    args = parser.parse_args()

    # Parse OWL ontology
    g = Graph().parse(args.input_ontology, format=args.ontology_format)
    # Convert to networkx
    digraph = produce_graph.produce_graph(g, options=args.options)

    # Write nodes
    with open(args.output_nodes, 'w') as f:
        to_visjs.write_nodes(digraph, f)

    # Write arcs
    with open(args.output_arcs, 'w') as f:
        to_visjs.write_arcs(digraph, f)


if __name__ == '__main__':
    main()
