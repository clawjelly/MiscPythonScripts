import collections

blue = [2,2,2,7,7,7]
magenta = [1,1,6,6,6,6]
olive = [0,5,5,5,5,5]
red = [9,4,4,4,4,4]
yellow = [3,3,3,3,8,8]
d6 = [1,2,3,4,5,6]

dices={
    "blue" : blue,
    "magenta" : magenta,
    "olive" : olive,
    "red" : red,
    "yellow" : yellow
}

t1 = [1,2]
t2 = [3,4]

def iterablep(x):
    return isinstance(x, collections.Iterable)

def wrap(lst):
    return [[x] if not iterablep(x) else x for x in lst]

def flat(x):
    return [item for sublist in x for item in sublist]

def flatten(x):
    return flat(wrap(x))

def cross(a, b):
    """
    Generates pairs of list a with list b.
    The returned list has a length of a*b.
    """
    return [[x, y] for x in a for y in b]

def left_side_wins(left, right):
    return len([x for x,y in cross(left, right) if x > y])

def twice(x):
    return map(sum, cross(x,x))

def triple(x):
    return map(sum, map(flatten,cross(cross(x,x),x)))

def quad(x):
    return twice(twice(x))

def report(x,y):
    games = len(cross(x,y))
    wins = left_side_wins(x,y)
    pwins = float(wins) / float(games) * 100
    print( "The left side won %i times out of %i matches" % (wins,games) )
    print( "That is %f4 percent" % pwins )

def main ():
    print( )
    print( "--- === Ring I === ---" )
    print( )
    print( "Blue vs Magenta" )
    report(blue, magenta)
    print( "Magenta vs Olive" )
    report(magenta, olive)
    print( "Olive vs Red" )
    report(olive, red)
    print( "Red vs Yellow" )
    report(red, yellow)
    print( "Red vs Blue" )
    report(red, blue)
    print( )
    print( "=== Two ===" )
    print( )
    print( "Two Blue vs Two Magenta" )
    report(twice(blue), twice(magenta))
    print( "Two Magenta vs Two Olive" )
    report(twice(magenta), twice(olive))
    print( "Two Olive vs Two Red" )
    report(twice(olive), twice(red))
    print( "Two Red vs Two Yellow" )
    report(twice(red), twice(yellow))
    print( "Two Yellow vs Two Blue" )
    report(twice(yellow), twice(blue))
    print( )
    print( "=== Three ===" )
    print( )
    print( "Three Blue vs Three Magenta" )
    report(triple(blue), triple(magenta))
    print( "Three Magenta vs Three Olive" )
    report(triple(magenta), triple(olive))
    print( "Three Olive vs Three Red" )
    report(triple(olive), triple(red))
    print( "Three Red vs Three Yellow" )
    report(triple(red), triple(yellow))
    print( "Three Yellow vs Three Blue" )
    report(triple(yellow), triple(blue))
    print( )
    print( "--- === Ring II === ---" )
    print( )
    print( "Red vs Blue" )
    report(red, blue)
    print( "Blue vs Olive" )
    report(blue, olive)
    print( "olive vs Yellow" )
    report(olive, yellow)
    print( "Yellow vs Magenta" )
    report(yellow, magenta)
    print( "Magenta vs Red" )
    report(magenta,red)
    print( )
    print( "=== Two ===" )
    print( )
    print( "Red vs Blue" )
    report(twice(red), twice(blue))
    print( "Blue vs Olive" )
    report(twice(blue), twice(olive))
    print( "Olive vs Yellow" )
    report(twice(olive), twice(yellow))
    print( "Yellow vs Magenta" )
    report(twice(yellow),twice(magenta))
    print( "Magenta vs Red" )
    report(twice(magenta),twice(red))
    print( )
    print( "=== Three ===" )
    print( )
    print( "Three Red vs Three Blue" )
    report(triple(red),triple(blue))
    print( "Three Blue vs Three Olive" )
    report(triple(blue),triple(olive))
    print( "Olive vs Yellow" )
    report(triple(olive),triple(yellow))
    print( "Yellow vs Magenta" )
    report(triple(yellow), triple(magenta))
    print( "Magenta vs Red" )
    report(triple(magenta),triple(red))
    print( )
    print( "=== Four ===" )
    print( "Four red vs Four Blue" )
    report(quad(red),quad(blue))
    print( "Four Blue vs Four Olive" )
    report(quad(blue),quad(blue))
    print( "Four Olive vs Four Yellow" )
    report(quad(olive),quad(yellow))
    print( "Four Yellow vs Four Magenta" )
    report(quad(yellow),quad(magenta))
    print( "Magenta vs Red" )
    report(quad(magenta),quad(red))

def compare_dice(diceA, diceB):
    games=0
    wins=0
    for sideA in diceA:
        for sideB in diceB:
            games+=1
            if sideA>sideB:
                wins+=1

    return {"games":games, "wins":wins, "ratio":int(wins/games*100) }


def play_all_games():
    
    dicesA=dices.copy()
    dicesB=dices.copy()
    for keyA, valueA in dicesA.items():
        dicesB.pop(keyA)
        if len(dicesB)!=0:
            for keyB, valueB in dicesB.items():
                result=compare_dice(valueA, valueB)
                print ("{} vs {}: {} games, {} wins - {}% won.".format(keyA, keyB, result["games"], result["wins"], result["ratio"]))


play_all_games()
