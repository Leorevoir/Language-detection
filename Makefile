##
## EPITECH PROJECT, 2024
## Language-detection
## File description:
## Makefile
##

.PHONY: all clean fclean re

CC = python3

PFLAGS = -m

NAME = unittest

all: $(NAME)

$(NAME):
	@$(CC) $(PFLAGS) $(NAME) -v data/unit_test.py
	@coverage run data/unit_test.py
	@coverage report $(PFLAGS)
	@printf "[\033[1;32mSUCCESS\033[0m] Compiled %s\n" $(NAME)

clean:
	@rm -rf __pycache__
	@rm -rf data/__pycache__
	@rm -rf script/__pycache__
	@printf "[\033[1;32mCLEAN\033[0m] Removed binary\n"

fclean: clean
	@rm -f $(NAME)
	@rm -f .coverage
	@rm -rf coding-style-reports.log
	@printf "[\033[1;32mFCLEAN\033[0m] Removed %s\n" $(NAME)

re: fclean all

.SILENT:
