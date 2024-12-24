def population_change(current_population, birth_rate, death_rate):
    birth_rate = birth_rate / 100
    death_rate = death_rate / 100
    births = current_population * birth_rate
    deaths = current_population * death_rate
    return round(current_population + births - deaths)






def main():
    from rich.console import Console
    console = Console()
    console.print("[bold green]POPULATION CHANGE OVER TIME[/bold green]")
    console.print("[bold red]----------------------------------[/bold red]")

    initial_population = int(console.input("[blue]Enter the current population: [/blue]"))
    birth_rate = int(console.input("[blue]Enter the birth rate: [/blue]"))
    death_rate = int(console.input("[blue]Enter the death rate: [/blue]"))
    time_period = int(console.input("[blue]Enter the time units: [/blue]"))
    carr_capacity = int(console.input("[blue]Enter the carrying capacity: [/blue]"))

    count = 1
    current_population = initial_population
    while count <= time_period:
        current_population = population_change(current_population, birth_rate, death_rate)
        console.print(f"[bold green]Year {count}: {current_population}[/bold green]")
        count += 1
    console.print(f"[bold green]The population after {time_period} years is {current_population}[/bold green]")
    if current_population > carr_capacity:
        console.print("[bold red]The population has exceeded the carrying capacity[/bold red]")
    else:
        console.print("[bold green]The population has not exceeded the carrying capacity[/bold green]")



    console.print("[bold red]----------------------------------[/bold red]")


if __name__ == "__main__":
    main()

