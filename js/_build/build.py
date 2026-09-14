import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from common import emit
from d1 import topics as d1
from d2 import topics as d2
from d3 import topics as d3
from d4 import topics as d4
from d5 import topics as d5


def validate(topics):
    ids = [t["id"] for t in topics]
    dup = [i for i, n in Counter(ids).items() if n > 1]
    if dup:
        raise SystemExit("Duplicate topic ids: " + ", ".join(dup))
    qids = []
    for t in topics:
        if t["domain"] not in (1, 2, 3, 4, 5):
            raise SystemExit("Bad domain on " + t["id"])
        if not t["quiz"]:
            raise SystemExit("No quiz on " + t["id"])
        for q in t["quiz"]:
            qids.append(q["id"])
            typ = q["type"]
            if typ == "single":
                assert len(q["choices"]) == 4, q["id"]
                assert q["answer"] == [q["answer"][0]]
                assert 0 <= q["answer"][0] < 4
            elif typ == "multi":
                assert len(q["choices"]) == 5, q["id"]
                assert len(q["answer"]) >= 2
                assert all(0 <= i < 5 for i in q["answer"])
            elif typ == "order":
                assert 3 <= len(q["items"]) <= 5, q["id"]
                assert sorted(q["answer"]) == list(range(len(q["items"])))
            elif typ == "match":
                assert 3 <= len(q["left"]) <= 7
                assert len(q["answer"]) == len(q["left"])
                assert all(0 <= i < len(q["right"]) for i in q["answer"])
            else:
                raise SystemExit("Bad type " + typ + " " + q["id"])
    dq = [i for i, n in Counter(qids).items() if n > 1]
    if dq:
        raise SystemExit("Duplicate question ids: " + ", ".join(dq))
    print(
        "OK",
        len(topics),
        "topics,",
        len(qids),
        "questions,",
        "by domain",
        {d: sum(1 for t in topics if t["domain"] == d) for d in range(1, 6)},
    )


def main():
    topics = d1() + d2() + d3() + d4() + d5()
    validate(topics)
    dest = HERE.parent / "topics.js"
    emit(topics, dest)


if __name__ == "__main__":
    main()
