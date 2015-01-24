from collections import namedtuple
from geosolver.text.syntax.misc import syntax_display_graphs
from geosolver.utils import display_graph

__author__ = 'minjoon'


class Syntax(object):
    def __init__(self, tokens, syntax_trees):
        assert isinstance(tokens, dict)
        assert isinstance(syntax_trees, dict)
        self.tokens = tokens
        self.syntax_trees = syntax_trees
        self.sentence = tokens[0].sentence

    def display_graphs(self):
        """
        Displays all syntax graphs.
        Used for debugging

        :return:
        """
        syntax_display_graphs(self)


class SyntaxTree(object):
    def __init__(self, graph, rank, score):
        self.graph = graph
        self.rank = rank
        self.score = score

    def display_graph(self):
        display_graph(self.graph)

    def __repr__(self):
        return "%s(rank=%d, score=%.2f)" % (self.__class__.__name__, self.rank, self.score)


class SyntaxPath(object):
    def __init__(self, syntax, tree_idx, tokens):
        self.syntax = syntax
        self.tree_idx = tree_idx
        self.tokens = tokens

    def __len__(self):
        return len(self.tokens)

