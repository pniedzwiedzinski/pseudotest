from pseudo import compile
from testing import Testing


def test(exercise, pseudocode, logger):

    # TODO: Get tests from RDS
    rds = {"a": [{"in": [1, 2], "out": [3]},
                 {"in": [234, 567], "out": [801]}]}
    tests = rds[exercise]

    instructions = compile(pseudocode)

    results = []

    for i, t in enumerate(tests):
        r = Testing(t["in"], t["out"])

        try:
            logger.info("Run test#"+str(i))
            r.run(instructions)
            if len(r.test_in) > 0 or len(r.test_out):
                raise AssertionError
            results.append(1)
        except (AssertionError, SystemExit):
            results.append(0)

    return results
