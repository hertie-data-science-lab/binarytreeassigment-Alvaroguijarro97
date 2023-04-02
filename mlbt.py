# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 15:31:59 2023

@author: Hannah
"""

from linkedbinarytree import LinkedBinaryTree


class MutableLinkedBinaryTree(LinkedBinaryTree):
    """
    Provides public wrapper functions for each of the inherited nonpublic update methods.
    """

    def add_root(self, e):
        return self._add_root(e)

    def add_left(self, p, e):
        return self._add_left(p, e)

    def add_right(self, p, e):
        return self._add_right(p, e)

    def replace(self, p, e):
        return self._replace(p, e)

    def delete(self, p):
        return self._delete(p)

    def attach(self, p, T1, T2):
        return self._attach(p, T1, T2)

    """Adding a way to visualize the tree"""
    def __str__(self):
        """Return a string representation of the tree in ASCII art format."""
        lines = self._build_lines(self.root())
        return "\n".join(lines)

    def _build_lines(self, position):
        """Recursively build a list of lines representing the subtree rooted at position."""
        if position is None:
            return []
        left_lines = self._build_lines(self.left(position))
        right_lines = self._build_lines(self.right(position))
        node_width = len(str(position.element()))
        left_width = len(left_lines[0]) if left_lines else 0
        right_width = len(right_lines[0]) if right_lines else 0
        total_width = node_width + left_width + right_width
        lines = []
        # Build the first line (node and left/right edges)
        left_padding = " " * left_width if left_width > 0 else ""
        right_padding = " " * right_width if right_width > 0 else ""
        node_line = f"{left_padding}{position.element()}{right_padding}"
        edge_line = f"{left_padding}{'/' if left_width > 0 else ' '}{right_padding}{'/'if right_width > 0 else ' '}"
        lines.append(node_line)
        lines.append(edge_line)
        # Build the remaining lines (left and right subtrees)
        for i in range(max(len(left_lines), len(right_lines))):
            left_line = left_lines[i] if i < len(left_lines) else " " * left_width
            right_line = right_lines[i] if i < len(right_lines) else " " * right_width
            line = f"{left_line}{' ' * node_width}{right_line}"
            lines.append(line)
        return lines
