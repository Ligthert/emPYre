# emPYre
(should change as soon as the game is more complete)

## About
EmPYre is an (experimental) python 3 implementation of the old Empire game.

### Why?
The current port on Ubuntu is slow AF and also the control-scheme like many tools from that era it didn't era very well. (ignoring features we see in modern open-source RTS-games these days)

# Requirements
* Python 3.4+

# Developer notes
TODO:
* Look into how the original version did the battle system ( units vs units vs cities )
* Look into ASCII, Colours, blinking and other flashy things
  * + land
  * . sea
  * ^ (mountains?)
* Look into nCurses to deal with the interface issues
  * Different parts of the screen
  * Pop-up a window if something is required?
* Look into how to do this
  * Separate the logic from the interface?
  * Multiple opponents?
  * Multi-player?
  * Multi-session multi-player?
* Modern systems
  * Waypoints?
  * Build-queues?
  * Patrols?

## Combat

```    while (att_obj->hits > 0 && def_obj->hits > 0) {
        if (irand (2) == 0) /* defender hits? */
            att_obj->hits -= piece_attr[def_obj->type].strength;
        else def_obj->hits -= piece_attr[att_obj->type].strength;
    }
```

|Piece|You|Enemy|Moves|Hits|Str|Cost|
| --- | ---| ---| ---| ---| ---| ---|
|Army|A|a|1|1|1|5(6)|
|Fighter|F|f|8|1|1|10(12)|
|Patrol Boat|P|p|4|1|1|15(18)|
|Destroyer|D|d|2|3|1|20(24)|
|Submarine|S|s|2|2|3|20(24)|
|Troop Transport|T|t|2|1|1|30(36)|
|Aircraft Carrier|C|c|2|8|1|30(36)|
|Battleship|B|b|2|10|2|40(48)|
|Satellite|Z|z|10|--|--|50(60)|

Other details: http://www.catb.org/~esr/vms-empire/vms-empire.html


```
typedef struct piece_attr {
        char sname; /* eg 'C' */
        char name[20]; /* eg "aircraft carrier" */
        char nickname[20]; /* eg "carrier" */
        char article[20]; /* eg "an aircraft carrier" */
        char plural[20]; /* eg "aircraft carriers" */
        char terrain[4]; /* terrain piece can pass over eg "." */
        uchar build_time; /* time needed to build unit */
        uchar strength; /* attack strength */
        uchar max_hits; /* number of hits when completely repaired */
        uchar speed; /* number of squares moved per turn */
        uchar capacity; /* max objects that can be held */
        long range; /* range of piece */
} piece_attr_t;
```
