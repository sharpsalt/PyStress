import os
import sys
import argparse
import platform
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from generators.generate_arrays import gen_arrays
from generators.generate_numbers import gen_numbers
from generators.generate_strings import gen_strings, CaseType
from generators.generate_graphs import gen_graphs


class StressTestGenerator:
    """
    Main stress testing data generator class.
    Provides methods to generate test cases for competitive programming.
    """
    
    def __init__(self):
        self.rng = None
    
    # ==================== ARRAY GENERATORS ====================
    
    @staticmethod
    def random_array(size, min_val, max_val, unique=False, sorted_=False):
        """Generate a random array."""
        return gen_arrays.random(size, min_val, max_val, unique=unique, sorted_=sorted_)
    
    @staticmethod
    def permutation(n):
        """Generate a random permutation of 1 to n."""
        return gen_arrays.permutation(n)
    
    @staticmethod
    def matrix(rows, cols, min_val, max_val):
        """Generate a random matrix."""
        return gen_arrays.matrix(rows, cols, min_val, max_val)
    
    @staticmethod
    def pairs(count, min_l, max_l, min_r, max_r, ordered=False):
        """Generate random pairs."""
        return gen_arrays.pairs(count, min_l, max_l, min_r, max_r, ordered=ordered)
    
    @staticmethod
    def subset(min_val, max_val, size, sorted_=False):
        """Generate a random subset."""
        return gen_arrays.subset(min_val, max_val, size, sorted_=sorted_)
    
    @staticmethod
    def partition(total, parts, min_val, max_val):
        """Partition a sum into k parts."""
        return gen_arrays.partition(total, parts, min_val, max_val)
    
    @staticmethod
    def strictly_increasing(size, start, min_step, max_step):
        """Generate strictly increasing sequence."""
        return gen_arrays.strictly_increasing(size, start, min_step, max_step)
    
    @staticmethod
    def strictly_decreasing(size, start, min_step, max_step):
        """Generate strictly decreasing sequence."""
        return gen_arrays.strictly_decreasing(size, start, min_step, max_step)
    
    @staticmethod
    def arithmetic_sequence(size, start, step):
        """Generate arithmetic progression."""
        return gen_arrays.arithmetic_progression(size, start, step)
    
    @staticmethod
    def geometric_sequence(size, start, ratio):
        """Generate geometric progression."""
        return gen_arrays.geometric_progression(size, start, ratio)
    
    # ==================== NUMBER GENERATORS ====================
    
    @staticmethod
    def random_int(min_val, max_val):
        """Generate a random integer."""
        return gen_numbers.random_int(min_val, max_val)
    
    @staticmethod
    def random_float(min_val, max_val):
        """Generate a random float."""
        return gen_numbers.random_real(min_val, max_val)
    
    @staticmethod
    def random_numbers(min_val, max_val, count):
        """Generate multiple random numbers."""
        return gen_numbers.random_range(min_val, max_val, count)
    
    @staticmethod
    def random_exclude(min_val, max_val, exclude_set):
        """Generate random number excluding certain values."""
        return gen_numbers.random_exclude(min_val, max_val, exclude_set)
    
    @staticmethod
    def weighted_choice(values, weights):
        """Choose from weighted distribution."""
        return gen_numbers.random_weighted(values, weights)
    
    # ==================== STRING GENERATORS ====================
    
    @staticmethod
    def random_string(length, case_type=CaseType.Mixed):
        """Generate random string."""
        return gen_strings.random(length, case_type)
    
    @staticmethod
    def random_palindrome(length, case_type=CaseType.Lower):
        """Generate random palindrome."""
        return gen_strings.palindrome(length, case_type)
    
    @staticmethod
    def random_alphanum(length, case_type=CaseType.Mixed):
        """Generate alphanumeric string."""
        return gen_strings.random_alphanum(length, True, True, case_type)
    
    @staticmethod
    def random_from_alphabet(length, alphabet):
        """Generate string from custom alphabet."""
        return gen_strings.random_custom(length, alphabet)
    
    @staticmethod
    def multiple_strings(count, length, case_type=CaseType.Mixed):
        """Generate multiple random strings."""
        return gen_strings.random_strings(count, length, case_type)
    
    # ==================== GRAPH GENERATORS ====================
    
    @staticmethod
    def tree(n_nodes, zero_based=False):
        """Generate random tree."""
        return gen_graphs.tree(n_nodes, zero_based=zero_based)
    
    @staticmethod
    def simple_graph(n_nodes, n_edges, zero_based=False):
        """Generate random simple graph."""
        return gen_graphs.simple_graph(n_nodes, n_edges, zero_based=zero_based)
    
    @staticmethod
    def weighted_graph(n_nodes, n_edges, min_weight, max_weight, zero_based=False):
        """Generate random weighted graph."""
        return gen_graphs.weighted_graph(n_nodes, n_edges, min_weight, max_weight, zero_based=zero_based)
    
    @staticmethod
    def directed_graph(n_nodes, n_edges, zero_based=False):
        """Generate random directed graph."""
        return gen_graphs.directed_graph(n_nodes, n_edges, zero_based=zero_based)
    
    @staticmethod
    def dag(n_nodes, n_edges, zero_based=False):
        """Generate random DAG (Directed Acyclic Graph)."""
        return gen_graphs.dag(n_nodes, n_edges, zero_based=zero_based)
    
    @staticmethod
    def bipartite_graph(n1, n2, n_edges, zero_based=False):
        """Generate random bipartite graph."""
        return gen_graphs.bipartite(n1, n2, n_edges, zero_based=zero_based)
    
    @staticmethod
    def cycle(n_nodes, zero_based=False):
        """Generate cycle graph."""
        return gen_graphs.cycle(n_nodes, zero_based=zero_based)
    
    @staticmethod
    def star_graph(n_nodes, center=1, zero_based=False):
        """Generate star graph."""
        return gen_graphs.star(n_nodes, center, zero_based=zero_based)
    
    @staticmethod
    def complete_graph(n_nodes, zero_based=False):
        """Generate complete graph."""
        return gen_graphs.complete(n_nodes, zero_based=zero_based)
    
    # ==================== OUTPUT FUNCTIONS ====================
    
    @staticmethod
    def format_array(arr, separator=' '):
        """Format array for output."""
        return separator.join(map(str, arr))
    
    @staticmethod
    def format_matrix(matrix, separator=' '):
        """Format matrix for output."""
        return '\n'.join(StressTestGenerator.format_array(row, separator) for row in matrix)
    
    @staticmethod
    def format_edges(edges, separator=' '):
        """Format edges for output."""
        lines = []
        for edge in edges:
            if isinstance(edge, tuple) and len(edge) == 2:
                lines.append(f"{edge[0]}{separator}{edge[1]}")
            elif isinstance(edge, tuple) and len(edge) == 3:
                lines.append(f"{edge[0]}{separator}{edge[1]}{separator}{edge[2]}")
        return '\n'.join(lines)
    
    @staticmethod
    def save_to_file(content, filename):
        """Save generated data to file."""
        with open(filename, 'w') as f:
            f.write(content)
        print(f"✓ Saved to {filename}")
    
    @staticmethod
    def load_from_file(filename):
        """Load test case from file."""
        with open(filename, 'r') as f:
            return f.read()


def main():
    """Command-line interface for stress testing."""
    parser = argparse.ArgumentParser(
        description='PyStress - Stress Testing Data Generator',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python stress_testing.py array --size 10 --min 1 --max 100
  python stress_testing.py tree --nodes 5
  python stress_testing.py string --length 15
  python stress_testing.py graph --type simple --nodes 6 --edges 10
        '''
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Generator type')
    
    # Array subcommand
    array_parser = subparsers.add_parser('array', help='Generate random array')
    array_parser.add_argument('--size', type=int, default=10, help='Array size')
    array_parser.add_argument('--min', type=int, default=1, help='Minimum value')
    array_parser.add_argument('--max', type=int, default=100, help='Maximum value')
    array_parser.add_argument('--unique', action='store_true', help='Unique elements')
    array_parser.add_argument('--sorted', action='store_true', help='Sorted array')
    array_parser.add_argument('--output', help='Save to file')
    
    # Number subcommand
    num_parser = subparsers.add_parser('number', help='Generate random number')
    num_parser.add_argument('--min', type=int, default=1, help='Minimum')
    num_parser.add_argument('--max', type=int, default=100, help='Maximum')
    num_parser.add_argument('--count', type=int, default=1, help='Count')
    num_parser.add_argument('--output', help='Save to file')
    
    # String subcommand
    str_parser = subparsers.add_parser('string', help='Generate random string')
    str_parser.add_argument('--length', type=int, default=10, help='String length')
    str_parser.add_argument('--case', choices=['lower', 'upper', 'mixed'], default='mixed')
    str_parser.add_argument('--count', type=int, default=1, help='Number of strings')
    str_parser.add_argument('--output', help='Save to file')
    
    # Graph subcommand
    graph_parser = subparsers.add_parser('graph', help='Generate random graph')
    graph_parser.add_argument('--type', choices=['tree', 'simple', 'weighted', 'directed', 'dag', 'bipartite'], default='simple')
    graph_parser.add_argument('--nodes', type=int, default=5, help='Number of nodes')
    graph_parser.add_argument('--edges', type=int, default=8, help='Number of edges')
    graph_parser.add_argument('--min-weight', type=int, default=1, help='Min edge weight')
    graph_parser.add_argument('--max-weight', type=int, default=10, help='Max edge weight')
    graph_parser.add_argument('--output', help='Save to file')
    
    args = parser.parse_args()
    
    gen = StressTestGenerator()
    result = None
    
    if args.command == 'array':
        result = gen.random_array(
            args.size, args.min, args.max,
            unique=args.unique, sorted_=args.sorted
        )
        output = gen.format_array(result)
        
    elif args.command == 'number':
        if args.count == 1:
            result = gen.random_int(args.min, args.max)
            output = str(result)
        else:
            result = gen.random_numbers(args.min, args.max, args.count)
            output = gen.format_array(result)
            
    elif args.command == 'string':
        case_map = {'lower': CaseType.Lower, 'upper': CaseType.Upper, 'mixed': CaseType.Mixed}
        if args.count == 1:
            result = gen.random_string(args.length, case_map[args.case])
            output = result
        else:
            result = gen.multiple_strings(args.count, args.length, case_map[args.case])
            output = '\n'.join(result)
            
    elif args.command == 'graph':
        if args.type == 'tree':
            result = gen.tree(args.nodes)
        elif args.type == 'simple':
            result = gen.simple_graph(args.nodes, args.edges)
        elif args.type == 'weighted':
            result = gen.weighted_graph(args.nodes, args.edges, args.min_weight, args.max_weight)
        elif args.type == 'directed':
            result = gen.directed_graph(args.nodes, args.edges)
        elif args.type == 'dag':
            result = gen.dag(args.nodes, args.edges)
        elif args.type == 'bipartite':
            result = gen.bipartite_graph(args.nodes // 2, args.nodes - args.nodes // 2, args.edges)
        
        output = gen.format_edges(result)
    
    else:
        parser.print_help()
        return
    
    print(output)
    
    if hasattr(args, 'output') and args.output:
        gen.save_to_file(output, args.output)


if __name__ == '__main__':
    main()