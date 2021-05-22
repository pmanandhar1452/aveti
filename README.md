# aveti
A sensor network (to monitor a home garden).

Aveti is a hobby project I created for pedagogical purposes. It illustrates the use of PyQt on a desktop frontend and gRPC on a Raspberry Pi for remote monitoring and watering of plants in a home garden.

The name is inspired by the Sanskrit word *अवेति*, which can mean among other things _to conceive_.

## Raspberry Pi Setup Tips

1. Make sure the server is run using a user who has dialout previliges
2. gpio libraries (We are using gpiozero: https://gpiozero.readthedocs.io/en/stable/)
    - https://gpiozero.readthedocs.io/en/stable/installing.html
