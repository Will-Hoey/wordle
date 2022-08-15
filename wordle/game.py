from dataclasses import dataclass, field


@dataclass
class Wordle:
    """
    An instance of a game where the objective is to match 2 words within a number of guesses.
    """

    word: str
    max_guesses: int  # Could base on difficulty?
    num_guesses: int = 0
    guesses: list = field(default_factory=lambda: [])
    incorrect_guessed_letters: list = field(default_factory=lambda: [])

    def _append_to_guesses(self, guess) -> None:
        self.guesses.append(guess)

    def _add_to_score(self) -> None:
        self.num_guesses += 1

    @property
    def has_game_finished(self) -> bool:
        return self.has_reached_max_guesses or self.has_guessed_correct_word

    @property
    def has_guessed_correct_word(self) -> bool:
        return self.word in self.guesses

    @property
    def has_reached_max_guesses(self) -> bool:
        return self.num_guesses >= self.max_guesses

    def check_letter(self, guess_word: str) -> list:
        """
        Checks the indices of the guess and word have the same letter
        """

        score = []
        for idx, letter in enumerate(guess_word):

            if letter in self.word:
                if letter == self.word[idx]:
                    score.append((letter, "green"))
                else:
                    score.append((letter, "yellow"))
            else:
                score.append((letter, "black"))
                self.incorrect_guessed_letters.append(letter)

        return score

    def check_guess(self, guess: str) -> list[tuple[int, str]]:
        """
        Checks a Guess word against the games word. Each guess will return a list the size of the
        guess with each element and either black, yellow or green..
            green = correct letter, correct index
            yellow = correct letter, wrong index
            black = incorrect letter
        """
        self._append_to_guesses(guess)
        self._add_to_score()

        if guess == self.word:
            return [(letter, "green") for letter in self.word]

        score = self.check_letter(guess)
        return score
