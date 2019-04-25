from pseudo import compile
from testing import Testing


def test(instruction, inp, out):
    r = Testing(inp, out)

    try:
        r.run(instructions)
        if len(r.test_in) > 0 or len(r.test_out):
            raise AssertionError
        return 1
    except (AssertionError, SystemExit):
        return 0


def run_tests(exercise, pseudocode, logger):

    # TODO: Get tests from RDS
    rds = {"a": [{"in": [1, 2], "out": [3]}, {"in": [234, 567], "out": [801]}]}
    tests = rds[exercise]

    instructions = compile(pseudocode)

    results = []

    for i, t in enumerate(tests):
        logger.info("Run test#" + str(i))
        test(instructions, t["in"], t["out"])

    return results
