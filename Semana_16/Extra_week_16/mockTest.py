import unittest
from unittest.mock import mock_open,patch
from readFile import read_lines


#Test Mock
class testReadLines(unittest.TestCase):
        def test_read_lines_successful(self):
            # 1. crear a fake file
            fake_file = mock_open(read_data="line1\nline2\nline3\n") 

            # 2. llamamos la funcion open y el parámetro(fake file)
            with patch("builtins.open", fake_file): 

            # 3. Llamamos a Readlines (la logica de la funcion)
                result = read_lines("fake_path.txt")

            # 4. Verificamos la salida
                self.assertEqual("".join(result), "line1\nline2\nline3\n")
        

        def test_read_lines_file_not_found_simple(self):
        # 1. llamamos a open pero el archivo no existe
         with patch("builtins.open", side_effect=FileNotFoundError):

            with self.assertRaises(FileNotFoundError):
                read_lines("no_fake_file.txt")

if __name__ == "__main__":
    unittest.main()