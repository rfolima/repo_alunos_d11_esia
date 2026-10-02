import sys
import unittest


def proposta_original(chamado, departamento):
    return (
        chamado["departamento"] == departamento
        and chamado["estado"] != "fechado"
    )


def proposta_ajustada(chamado, departamento):
    return chamado["departamento"] == departamento


CASOS = [
    (
        {"id": "V-01", "departamento": "Oficina",
         "estado": "aberto", "impacto": 1, "urgencia": 1},
        True,
    ),
    (
        {"id": "V-02", "departamento": "Oficina",
         "estado": "fechado", "impacto": 1, "urgencia": 1},
        True,
    ),
    (
        {"id": "V-03", "departamento": "Laborat\u00f3rio",
         "estado": "aberto", "impacto": 3, "urgencia": 3},
        False,
    ),
    (
        {"id": "V-04", "departamento": "Laborat\u00f3rio",
         "estado": "fechado", "impacto": 3, "urgencia": 3},
        False,
    ),
]


class TestVisibilidade(unittest.TestCase):
    funcao = staticmethod(proposta_ajustada)

    def test_quatro_casos_conforme_r3(self):
        for chamado, esperado in CASOS:
            with self.subTest(caso=chamado["id"]):
                retorno = self.funcao(chamado, "Oficina")
                print(
                    f'{chamado["id"]}: '
                    f'esperado={esperado}, retorno={retorno}',
                    flush=True,
                )
                self.assertEqual(retorno, esperado)


if __name__ == "__main__":
    if "--original" in sys.argv:
        TestVisibilidade.funcao = staticmethod(proposta_original)
        sys.argv.remove("--original")
    unittest.main(verbosity=2)
