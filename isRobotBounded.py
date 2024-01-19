from collections import namedtuple

class Solution(object):
    def isRobotBounded(self, instructions):
        positions = []  

        def anti_clock(side):
            if side == "North":
                return "West"
            elif side == "West":
                return "South"
            elif side == "South":
                return "East"
            elif side == "East":
                return "North"

        def clock(side):
            if side == "North":
                return "East"
            elif side == "West":
                return "North"
            elif side == "South":
                return "West"
            elif side == "East":
                return "South"

        Position = namedtuple("Position", ["x", "y", "direction"])
        current_position = Position(0, 0, "North")
        positions.append(current_position)

        instruct = list(instructions)
        for ch in instruct:
            if ch == 'L':
                current_direction = current_position.direction
                new_direction = anti_clock(current_direction)
                new_position = Position(current_position.x, current_position.y, new_direction)
                current_position = new_position
                positions.append(current_position)
            elif ch == 'R':
                current_direction = current_position.direction
                new_direction = clock(current_direction)
                new_position = Position(current_position.x, current_position.y, new_direction)
                current_position = new_position
                positions.append(current_position)
            elif ch == 'G':
                if current_position.direction == "North":
                    new_position = Position(current_position.x, current_position.y + 1, current_position.direction)
                elif current_position.direction == "West":
                    new_position = Position(current_position.x - 1, current_position.y, current_position.direction)
                elif current_position.direction == "South":
                    new_position = Position(current_position.x, current_position.y - 1, current_position.direction)
                elif current_position.direction == "East":
                    new_position = Position(current_position.x + 1, current_position.y, current_position.direction)

                current_position = new_position
                positions.append(current_position)

        return current_position == positions[0] or current_position.direction != "North"
