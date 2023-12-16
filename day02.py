from pydantic import BaseModel


class Game(BaseModel):
    id: int
    blue: list[int] = 0
    red: list[int] = 0
    green: list[int] = 0

    def set_value(self, color, value):
        self.__setattr__(color, max(self.__getattribute__(color), value))


def solve(version):
    ans = 0

    with open("input02.txt") as f:
        lines = f.readlines()
        for line in lines:
            a, b = line.split(":")
            game_id = int(a.split(" ")[1])

            game = Game(id=game_id)

            picks = b.split(";")
            for pick in picks:
                for color in pick.split(","):
                    n, c = color.strip().split(" ")
                    game.set_value(c, int(n))

            if (version == 1) and not (
                (game.blue > 14) or
                (game.red > 12) or
                (game.green > 13)
            ):
                ans += game.id

            if (version == 2):
                ans += game.blue * game.red * game.green

    print(ans)


if __name__ == "__main__":
    solve(1)
    solve(2)
