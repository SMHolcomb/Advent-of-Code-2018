
"""
************************************************************************************************
--- Day 14: Chocolate Charts ---


The Elves are trying to come up with the ultimate hot chocolate recipe; they're even maintaining 
a scoreboard which tracks the quality score (0-9) of each recipe.

Only two recipes are on the board: the first recipe got a score of 3, the second, 7. Each of 
the two Elves has a current recipe: the first Elf starts with the first recipe, and the second 
Elf starts with the second recipe.

To create new recipes, the two Elves combine their current recipes. This creates new recipes 
from the digits of the sum of the current recipes' scores. With the current recipes' scores of 
3 and 7, their sum is 10, and so two new recipes would be created: the first with score 1 and 
the second with score 0. If the current recipes' scores were 2 and 3, the sum, 5, would only 
create one recipe (with a score of 5) with its single digit.

The new recipes are added to the end of the scoreboard in the order they are created. So, 
after the first round, the scoreboard is 3, 7, 1, 0.

After all new recipes are added to the scoreboard, each Elf picks a new current recipe. To 
do this, the Elf steps forward through the scoreboard a number of recipes equal to 1 plus 
the score of their current recipe. So, after the first round, the first Elf moves forward 
1 + 3 = 4 times, while the second Elf moves forward 1 + 7 = 8 times. If they run out of 
recipes, they loop back around to the beginning. After the first round, both Elves happen 
to loop around until they land on the same recipe that they had in the beginning; in general, 
they will move to different recipes.

What are the scores of the ten recipes immediately after the number of recipes in your puzzle input?


# MY PUZZLE INPUT:  894501

--- Part Two ---

--- Part Two ---
As it turns out, you got the Elves' plan backwards. They actually want to know how many 
recipes appear on the scoreboard to the left of the first recipes whose scores are 
the digits from your puzzle input.

************************************************************************************************

Completed:  1/2/19

************************************************************************************************
"""




def main():

    RECIPES = 894501

    # PART I
    
    scores=''
    scores +='37'
    elf_1 = 0
    elf_2 = 1
    
    print(scores)

    while len(scores) < RECIPES+10:
        new_recipe = str(int(scores[elf_1]) + int(scores[elf_2]))
        scores+=new_recipe

        elf_1 = ( ( 1 + int(scores[elf_1]) + elf_1 ) % len(scores) )
        elf_2 = ( ( 1 + int(scores[elf_2])  + elf_2) % len(scores) )


    print("Part I:", scores[RECIPES:RECIPES+10])
    
    # PART II

    scores=''
    scores +='37'
    elf_1 = 0
    elf_2 = 1

    while str(RECIPES) not in scores[-7:]:
        new_recipe = str(int(scores[elf_1]) + int(scores[elf_2]))
        scores+=new_recipe

        elf_1 = ( ( 1 + int(scores[elf_1]) + elf_1 ) % len(scores) )
        elf_2 = ( ( 1 + int(scores[elf_2])  + elf_2) % len(scores) )

    print( "Part II:", len(scores) - len(str(RECIPES))-1 )

if __name__ == "__main__":
    main()
