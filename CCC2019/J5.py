import itertools

# Number of pages in the book
num_pages = int(input())

# List of lists containing the options for each page
page_options = []

# Load data from standard input
for page in range(num_pages):
    options_for_page = [int(value) for value in input().split()[1:]]
    page_options.append(options_for_page)

# Start by reaching the first page
pages_reached = [1]

# Variables to contain the shortest path and whether or not all pages can be reached
shortest_path = None
all_done = None

# Remember how many pages were reached on the last run of the loop
last_num_pages_reached = len(pages_reached)

# Start an endless loop to explore the book
for i in itertools.count():
    # Iterate over each page that has been reached so far and look at the options
    for page in pages_reached.copy():
        # Get the options for this page (pages are 1-indexed so subtract 1)
        options = page_options[page - 1]
        # If there are no options, we have found the shortest path (add 1 because we start the loop having already reached page 0)
        if not options and shortest_path is None:
            shortest_path = i + 1
        # Iterate over each of the options for this page
        for option in options:
            # If the page has not already been reached, add it to the list (this prevents duplicates from being added)
            if option not in pages_reached:
                pages_reached.append(option)

    # After checking all the pages reached so far, check if we've found any new pages
    # If not, there are no more reachable pages in the book
    if len(pages_reached) == last_num_pages_reached:
        # Check whether the number of pages reached is equal to the total number of pages in the book
        all_done = 'Y' if (len(pages_reached) == num_pages) else 'N'
        # Exit out of the loop, as there's nothing more to find
        break
    # Store the number of pages reached on this iteration so we can use it on the next iteration
    last_num_pages_reached = len(pages_reached)

# Print the output values
print(all_done)
print(shortest_path)
