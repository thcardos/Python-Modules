import typing
import random


def consume_event(event_list: list[tuple[str, str]]
                  ) -> typing.Generator[tuple[str, str], None, None]:
    while event_list:
        event = random.choice(event_list)
        event_list.remove(event)
        yield (event)


def gen_event(name: list[str], action: list[str]
              ) -> typing.Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(name), random.choice(action))


def ft_data_stream() -> None:
    name = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot"]
    action = ["flee", "get away", "hide",
              "run away", "escape", "avoid", "flight"]
    events = gen_event(name, action)
    for i in range(1000):
        player, act = next(events)
        print(f"Event {i}: Player {player} did action {act}")
    event_list: list[tuple[str, str]] = []
    for i in range(10):
        event_list = event_list + [next(events)]
    print(f"Built list of 10 events: {event_list}")
    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


def main() -> None:
    print("=== Game Data Stream Processor ===")
    ft_data_stream()


if __name__ == "__main__":
    main()
