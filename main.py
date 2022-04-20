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
