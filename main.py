from internal_logic import *
from file_parsing import *
import sys

# ожидается ввод типа <name of the file> <path_to_parameters> <path_to_nodes>
# связанные файлы, указанные в импортах сверху, должны лежать в той же папке
parser = Parser()
state = parser.parse(sys.argv[1], sys.argv[2])
state.start()
