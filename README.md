## Game Of Numbers

It's Hard to beat it Haha!

## How to play

This game is an easy to understand game, you have 3 characters ```V: Vrai (True) F: Faux (False) and D: Deplace (Move) ```

There's two opponents, both of them have to guess a number of 4 digits eg. ```1245``` and ```3744```

The First opponent is the computer (script) will guess your number let's say it give you  ```1734```

You have to reply with 4 char ```VFFD``` that means the first char is in the right place ```7``` and ```3``` doesn't exist in the client number and ```4``` exist but not in the right place


## Usage

```python
from pygameofnumbers import Game, TerminalColors


def colors(s: str, c: TerminalColors):
    return f'{c}{s}{TerminalColors.ENDC}'


if __name__ == '__main__':
    game = Game()
    # print(f"BOT NUMBER: {game.bot_number}")
    while True:
        if len(game.true) < 4: # 7680
            # print(f'INFO: true: {game.true} - move: {game.move} - left: {game.left_numbers} - false: {game.false} - Predict: {game.worker()}')
            print(f"ROUTE: {game.route} Predicted Number: {colors(game.predict_number, TerminalColors.OKBLUE)}")
            solve = input("SOLVE: ")
            message = game.next(solve)
            if message is not None:
                print(f'error: {message}')

            client_predict = input("PREDICT MY NUMBER: ")
            situation = game.check_prediction(client_predict)
            print(f'RESULT: {colors(situation, TerminalColors.GOLD)}')
        else:
            print(f'I WIN :)')
            print(f'My Number Was: {game.bot_number}')
            print(f"You didn't know it Haha!")
            break

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)