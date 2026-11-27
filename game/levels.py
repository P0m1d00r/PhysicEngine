from engine.classes import WorldObject, Rectangle, Circle, Position

levels = [
    [
        [
            # floor
            WorldObject(mass=0, position=Position(30.5, 1.75), mesh=Rectangle(width=61, height=2.5), rotation=0, restitution=0, color='#4d3f38'),
            WorldObject(mass=0, position=Position(71, 1.75), mesh=Rectangle(width=8, height=2.5), rotation=0, restitution=0, color='#4d3f38'),
            WorldObject(mass=0, position=Position(50, 0.25), mesh=Rectangle(width=100, height=0.5), rotation=0, restitution=0, color='#4d3f38'),

            # jumps
            WorldObject(mass=0, position=Position(6, 3.5), mesh=Rectangle(width=1, height=1), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(8, 4), mesh=Rectangle(width=1, height=2), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(10, 4.5), mesh=Rectangle(width=1, height=3), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(12, 5), mesh=Rectangle(width=1, height=4), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(14, 5.5), mesh=Rectangle(width=1, height=5), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(16, 6), mesh=Rectangle(width=1, height=6), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(18, 6.5), mesh=Rectangle(width=1, height=7), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(20, 7), mesh=Rectangle(width=1, height=8), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(22, 7.5), mesh=Rectangle(width=1, height=9), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(24, 8), mesh=Rectangle(width=1, height=10), rotation=0, restitution=0.5, color='#bdaa97'),

            # green jumps
            WorldObject(mass=0, position=Position(27, 3.5), mesh=Rectangle(width=5, height=1), rotation=0, restitution=1, color='#8b9150'),
            WorldObject(mass=0, position=Position(30, 8), mesh=Rectangle(width=1, height=10), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(32, 3.5), mesh=Rectangle(width=3, height=1), rotation=0, restitution=1, color='#8b9150'),
            WorldObject(mass=0, position=Position(33, 10.5), mesh=Rectangle(width=1, height=11), rotation=0, restitution=0.5, color='#bdaa97'),

            # stairs
            WorldObject(mass=20, position=Position(36, 3.75), mesh=Rectangle(width=1.5, height=1.5), rotation=0, restitution=0, color='#8888dd'),
            WorldObject(mass=0, position=Position(43.5, 4.5), mesh=Rectangle(width=1.5, height=3), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(45, 5.25), mesh=Rectangle(width=1.5, height=4.5), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(46.5, 6), mesh=Rectangle(width=1.5, height=6), rotation=0, restitution=0.5, color='#bdaa97'),

            # floor square
            WorldObject(mass=30, position=Position(52, 4), mesh=Rectangle(width=4.5, height=2), rotation=0, restitution=0, color='#8888dd'),

            # wall
            WorldObject(mass=0, position=Position(74.5, 20.25), mesh=Rectangle(width=1, height=34.5), rotation=0, restitution=0.5, color='#bdaa97'),

            WorldObject(mass=0, position=Position(73, 4.75), mesh=Rectangle(width=2, height=0.5), rotation=0, restitution=1, color='#8b9150'),
            WorldObject(mass=0, position=Position(71, 6.75), mesh=Rectangle(width=2, height=0.5), rotation=0, restitution=1, color='#8b9150'),
            WorldObject(mass=0, position=Position(73, 8.75), mesh=Rectangle(width=2, height=0.5), rotation=0, restitution=1, color='#8b9150'),
            WorldObject(mass=0, position=Position(71, 10.75), mesh=Rectangle(width=2, height=0.5), rotation=0, restitution=1, color='#8b9150'),
            WorldObject(mass=0, position=Position(73, 12.75), mesh=Rectangle(width=2, height=0.5), rotation=0, restitution=1, color='#8b9150'),

            # 2nd floor
            WorldObject(mass=0, position=Position(22, 16.5), mesh=Rectangle(width=44, height=1), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(59, 16.5), mesh=Rectangle(width=22, height=1), rotation=0, restitution=0.5, color='#bdaa97'),

            # small wall
            WorldObject(mass=0, position=Position(61.5, 18.5), mesh=Rectangle(width=1, height=3), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=20, position=Position(65.75, 17.75), mesh=Rectangle(width=1.5, height=1.5), rotation=0, restitution=1, color='#8888dd'),

            # hole
            WorldObject(mass=0, position=Position(46, 13.75), mesh=Rectangle(width=6, height=0.5), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(43.5, 15), mesh=Rectangle(width=1, height=2), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(48.5, 15), mesh=Rectangle(width=1, height=2), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=30, position=Position(56.5, 18.5), mesh=Rectangle(width=3, height=3), rotation=0, restitution=0, color='#8888dd'),

            # stairs
            WorldObject(mass=0, position=Position(20, 17.75), mesh=Rectangle(width=1, height=1.5), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(18, 18.5), mesh=Rectangle(width=1, height=3), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(16, 19.25), mesh=Rectangle(width=1, height=4.5), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(7, 20), mesh=Rectangle(width=14, height=6), rotation=0, restitution=0.5, color='#bdaa97'),

        ],

        WorldObject(mass=0, position=Position(3, 23.5), mesh=Rectangle(width=1, height=1), rotation=0, restitution=0.5, color='#00ff00'),
    ],
    [
        [
            # floor
            WorldObject(mass=0, position=Position(10, 1.75), mesh=Rectangle(width=20, height=2.5), rotation=0, restitution=0, color='#4d3f38'),
            WorldObject(mass=0, position=Position(51, 1.75), mesh=Rectangle(width=48, height=2.5), rotation=0, restitution=0, color='#4d3f38'),
            WorldObject(mass=0, position=Position(37.5, 0.25), mesh=Rectangle(width=75, height=0.5), rotation=0, restitution=0, color='#4d3f38'),

            # boxes
            WorldObject(mass=30, position=Position(9, 4.25), mesh=Rectangle(width=4, height=2.5), rotation=0, restitution=0, color='#8888dd'),
            WorldObject(mass=30, position=Position(14.25, 4.25), mesh=Rectangle(width=2.5, height=2.5), rotation=0, restitution=0, color='#8888dd'),

            # stairs + bounces
            WorldObject(mass=0, position=Position(30, 3.75), mesh=Rectangle(width=1, height=1.5), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(32, 4.5), mesh=Rectangle(width=1, height=3), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(34, 5.25), mesh=Rectangle(width=1, height=4.5), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(36, 6), mesh=Rectangle(width=1, height=6), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(38, 6.75), mesh=Rectangle(width=1, height=7.5), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(40, 7.5), mesh=Rectangle(width=1, height=9), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(43.5, 3.25), mesh=Rectangle(width=5, height=0.5), rotation=0, restitution=1, color='#8b9150'),
            WorldObject(mass=0, position=Position(47, 7.25), mesh=Rectangle(width=1, height=8.5), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(50.5, 3.25), mesh=Rectangle(width=5, height=0.5), rotation=0, restitution=1, color='#8b9150'),
            WorldObject(mass=0, position=Position(54, 7), mesh=Rectangle(width=1, height=8), rotation=0, restitution=0.5, color='#bdaa97'),

            # ladder to floor 2
            #WorldObject(mass=0, position=Position(74.5, 20.25), mesh=Rectangle(width=1, height=34.5), rotation=0, restitution=0, color='#bdaa97'),
            WorldObject(mass=0, position=Position(73, 4.75), mesh=Rectangle(width=2, height=0.5), rotation=0, restitution=1, color='#8b9150'),
            WorldObject(mass=0, position=Position(69.5, 6.75), mesh=Rectangle(width=2, height=0.5), rotation=0, restitution=1, color='#8b9150'),
            WorldObject(mass=0, position=Position(73, 8.75), mesh=Rectangle(width=2, height=0.5), rotation=0, restitution=1, color='#8b9150'),
            WorldObject(mass=0, position=Position(69.5, 10.75), mesh=Rectangle(width=2, height=0.5), rotation=0, restitution=1, color='#8b9150'),
            WorldObject(mass=0, position=Position(73, 12.75), mesh=Rectangle(width=2, height=0.5), rotation=0, restitution=1, color='#8b9150'),
            WorldObject(mass=0, position=Position(69.5, 14.75), mesh=Rectangle(width=2, height=0.5), rotation=0, restitution=1, color='#8b9150'),

            # 2nd floor
            WorldObject(mass=0, position=Position(16, 15.5), mesh=Rectangle(width=32, height=1), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(39.5, 15.5), mesh=Rectangle(width=9, height=1), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(51.5, 15.5), mesh=Rectangle(width=9, height=1), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(63.5, 15.5), mesh=Rectangle(width=9, height=1), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(45.5, 28), mesh=Rectangle(width=7, height=19), rotation=0, restitution=0.5, color='#bdaa97'),

            # finish
            WorldObject(mass=20, position=Position(20, 16.75), mesh=Rectangle(width=1.5, height=1.5), rotation=0, restitution=1, color='#8888dd'),
            WorldObject(mass=0, position=Position(6, 17.5), mesh=Rectangle(width=12, height=3), rotation=0, restitution=0.5, color='#bdaa97'),
        ],

        WorldObject(mass=0, position=Position(3, 19.5), mesh=Rectangle(width=1, height=1), rotation=0, restitution=0.5, color='#00ff00'),
    ],
    [
        [
            # floor
            WorldObject(mass=0, position=Position(20, 1.75), mesh=Rectangle(width=40, height=2.5), rotation=0, restitution=0, color='#4d3f38'),
            WorldObject(mass=0, position=Position(68.5, 1.75), mesh=Rectangle(width=13, height=2.5), rotation=0, restitution=0, color='#4d3f38'),
            WorldObject(mass=0, position=Position(37.5, 0.25), mesh=Rectangle(width=75, height=0.5), rotation=0, restitution=0, color='#4d3f38'),

            # stairs
            WorldObject(mass=0, position=Position(5, 3.75), mesh=Rectangle(width=1, height=1.5), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(7, 4.5), mesh=Rectangle(width=1, height=3), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(9, 5.25), mesh=Rectangle(width=1, height=4.5), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(11, 6), mesh=Rectangle(width=1, height=6), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(13, 6.75), mesh=Rectangle(width=1, height=7.5), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(27, 11.5), mesh=Rectangle(width=26, height=1), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(15.5, 7), mesh=Rectangle(width=1, height=8), rotation=0, restitution=0.5, color='#bdaa97'),

            # box
            WorldObject(mass=30, position=Position(25, 12.75), mesh=Rectangle(width=3, height=1.5), rotation=0, restitution=0, color='#8888dd'),

            # ladder
            WorldObject(mass=0, position=Position(74.5, 20.25), mesh=Rectangle(width=1, height=34.5), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(69, 4.25), mesh=Rectangle(width=2, height=0.5), rotation=0, restitution=1, color='#8b9150'),
            WorldObject(mass=0, position=Position(73, 5.75), mesh=Rectangle(width=2, height=0.5), rotation=0, restitution=1, color='#8b9150'),
            WorldObject(mass=0, position=Position(69, 7.25), mesh=Rectangle(width=2, height=0.5), rotation=0, restitution=1, color='#8b9150'),
            WorldObject(mass=0, position=Position(73, 8.75), mesh=Rectangle(width=2, height=0.5), rotation=0, restitution=1, color='#8b9150'),
            WorldObject(mass=0, position=Position(69, 10.25), mesh=Rectangle(width=2, height=0.5), rotation=0, restitution=1, color='#8b9150'),
            WorldObject(mass=0, position=Position(73, 11.75), mesh=Rectangle(width=2, height=0.5), rotation=0, restitution=1, color='#8b9150'),
            WorldObject(mass=0, position=Position(69, 13.25), mesh=Rectangle(width=2, height=0.5), rotation=0, restitution=1, color='#8b9150'),
            WorldObject(mass=0, position=Position(73, 14.75), mesh=Rectangle(width=2, height=0.5), rotation=0, restitution=1, color='#8b9150'),
            WorldObject(mass=0, position=Position(69, 16.25), mesh=Rectangle(width=2, height=0.5), rotation=0, restitution=1, color='#8b9150'),
            WorldObject(mass=0, position=Position(73, 17.75), mesh=Rectangle(width=2, height=0.5), rotation=0, restitution=1, color='#8b9150'),
            WorldObject(mass=0, position=Position(69, 19.25), mesh=Rectangle(width=2, height=0.5), rotation=0, restitution=1, color='#8b9150'),
            WorldObject(mass=0, position=Position(73, 20.75), mesh=Rectangle(width=2, height=0.5), rotation=0, restitution=1, color='#8b9150'),
            WorldObject(mass=0, position=Position(69, 22.25), mesh=Rectangle(width=2, height=0.5), rotation=0, restitution=1, color='#8b9150'),
            WorldObject(mass=0, position=Position(73, 23.75), mesh=Rectangle(width=2, height=0.5), rotation=0, restitution=1, color='#8b9150'),
            WorldObject(mass=0, position=Position(69, 25.25), mesh=Rectangle(width=2, height=0.5), rotation=0, restitution=1, color='#8b9150'),

            # top floor
            WorldObject(mass=0, position=Position(27.5, 25.5), mesh=Rectangle(width=15, height=1), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(44, 25.5), mesh=Rectangle(width=12, height=1), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(60.5, 25.5), mesh=Rectangle(width=15, height=1), rotation=0, restitution=0.5, color='#bdaa97'),

            # platforms
            WorldObject(mass=0, position=Position(16, 26.25), mesh=Rectangle(width=2, height=0.5), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(11, 27.25), mesh=Rectangle(width=2, height=0.5), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(3.5, 28), mesh=Rectangle(width=7, height=1), rotation=0, restitution=0.5, color='#bdaa97'),
        ],

        WorldObject(mass=0, position=Position(3, 29), mesh=Rectangle(width=1, height=1), rotation=0, restitution=0.5, color='#00ff00'),
    ],
    [
        [
            # floor
            WorldObject(mass=0, position=Position(29, 1.75), mesh=Rectangle(width=58, height=2.5), rotation=0, restitution=0, color='#4d3f38'),
            WorldObject(mass=0, position=Position(69, 1.75), mesh=Rectangle(width=12, height=2.5), rotation=0, restitution=0, color='#4d3f38'),
            WorldObject(mass=0, position=Position(37.5, 0.25), mesh=Rectangle(width=75, height=0.5), rotation=0, restitution=0, color='#4d3f38'),


            # jump walls
            WorldObject(mass=0, position=Position(22.5, 3.25), mesh=Rectangle(width=5, height=0.5), rotation=0, restitution=1, color='#8b9150'),
            WorldObject(mass=0, position=Position(27, 16.5), mesh=Rectangle(width=1, height=27), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(30.5, 3.25), mesh=Rectangle(width=5, height=0.5), rotation=0, restitution=1, color='#8b9150'),
            WorldObject(mass=0, position=Position(35, 16), mesh=Rectangle(width=1, height=26), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(38.5, 3.25), mesh=Rectangle(width=5, height=0.5), rotation=0, restitution=1, color='#8b9150'),
            WorldObject(mass=0, position=Position(43, 15.5), mesh=Rectangle(width=1, height=25), rotation=0, restitution=0.5, color='#bdaa97'),

            # box
            WorldObject(mass=30, position=Position(50, 4.25), mesh=Rectangle(width=4, height=2.5), rotation=0, restitution=0, color='#8888dd'),

            # finish
            WorldObject(mass=0, position=Position(68.5, 20.9), mesh=Rectangle(width=7, height=33.2), rotation=0, restitution=0.5, color='#bdaa97'),
            WorldObject(mass=0, position=Position(74.5, 20.25), mesh=Rectangle(width=1, height=34.5), rotation=0, restitution=0.5, color='#bdaa97'),
        ],

        WorldObject(mass=0, position=Position(73, 3.5), mesh=Rectangle(width=1, height=1), rotation=0, restitution=0.5, color='#00ff00'),
    ],
]