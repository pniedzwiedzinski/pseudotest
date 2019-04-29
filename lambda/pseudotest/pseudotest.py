from pseudo import compile
from .testing import Testing
from .get_test import get_test


def test(instructions, inp, out):
    r = Testing(inp, out)

    try:
        r.run(instructions)
        if len(r.test_in) > 0 or len(r.test_out):
            raise AssertionError
        return 1
    except (AssertionError, SystemExit):
        return 0


def run_tests(exercise, pseudocode, logger):

    tests = get_test(exercise)

    instructions = compile(pseudocode)

    results = []

    for i, t in enumerate(tests):
        logger.info("Run test#" + str(i))
        r = test(instructions, t["test_in"], t["test_out"])
        results.append(r)

    return results
