##
## EPITECH PROJECT, 2024
## Language-detection
## File description:
## Makefile
##

.PHONY: all clean fclean re result

CC = python3

PFLAGS = -m

NAME = unittest

all: $(NAME) result

$(NAME):
	@$(CC) $(PFLAGS) unittest -v data/unit_test.py
	@coverage run data/unit_test.py
	@coverage report

result:
	@COVERAGE_PERCENT=$$(coverage report | grep 'TOTAL' \
	| awk '{print $$NF}' | sed 's/%//'); \
	if [ $$COVERAGE_PERCENT -lt 50 ]; then \
		printf "[\033[1;31mFF :(\033[0m] Low Coverage: %s%%\n" $$COVERAGE_PERCENT; \
	else \
		printf "[\033[1;33mGG !\033[0m] Good Coverage: %s%%\n" $$COVERAGE_PERCENT; \
	fi
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
