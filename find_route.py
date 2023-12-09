from my_queue import MyQueue
from stack import Stack

__author__ = 'Brandon Plyler'


def reset(all_cities):
    """
    Mark all cities in the dictionary as True, i.e. not visited
    :param all_cities: dictionary listing all cities
    :return: None
    """
    for w in all_cities:
        all_cities.__setitem__(w, True)


def read_flights(filename):
    """
    Reads the referenced text file
    and returns two dictionaries as described below

    :param filename: file with the flight data
    :return: two dictionaries
                 dictionary 1: key = city, value = list of tuples corresponding to destinations as described in file
                 dictionary 2: key = city, value = True
    """
    import ast
    file = open(filename, "r")
    flights = {}
    cities = {}
    for line in file:
        line = line.strip()
        source, dest = line.split(':')
        flights[source] = ast.literal_eval(dest)
        cities[source] = True

    return flights, cities


def get_next_cities(current_city, dictionary):
    """
    Returns a list representing cities that are directly reachable from current_city

    Parameters:
        current_city: some city
        dictionary: represents the dictionary that we will be getting the list from
    Returns:
        list representing cities with direct flights from current city
    """
    result = []
    cities = dictionary.get(str(current_city))
    for item in cities:
        result.append(item[0])
    return result


def find_route(start_city, end_city, all_flights, all_cities):
    """
    Finds the shortest route between the start city and end city

    Parameters:
        start_city: the start city
        end_city:  the end city
        all_flights: dictionary describing all flights
        all_cities: dictionary corresponding to all cities
    Returns:
        A stack corresponding to the shortest route between start_city and end_city, or None if no route exists
    """
    s = Stack()
    q = MyQueue()
    s.push(start_city)
    q.enqueue(s)
    while not q.is_empty():
        stk = q.dequeue()
        city = stk.peek()
        not_visited = all_cities.get(str(city))
        if city == end_city:
            return stk, q.size()
        elif not_visited:
            reachable_cities = get_next_cities(city, all_flights)
            for item in reachable_cities:
                clones = stk.clone()
                clones.push(item)
                all_cities.__setitem__(str(city), False)
                q.enqueue(clones)
    return None, q.size()


def main():
    """
    Main function that outputs the route between teh two cities entered or if no route can be found,
    then outputs "There is no route between start_city and end city :("

    Parameters:

    Returns:
        The route and length of the queue or no route between the two cities

    """
    all_flights, all_cities = read_flights("Resources/flights.txt")
    start_city = input(str('Enter Start City:'))
    end_city = input(str('Enter End City:'))
    route, size = find_route(start_city, end_city, all_flights, all_cities)
    if route is None:
        print('There is no route between', start_city, 'and', end_city, ':(')
    else:
        print('This Is Your Route:', route)
        print('Queue Length:', size)


main()
