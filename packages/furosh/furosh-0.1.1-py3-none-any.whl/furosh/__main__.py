import click

@click.command()
@click.argument('command')
def main(command):
    if command == 'hello':
        click.echo('Hello, World!')
    else:
        click.echo(f"Unknown command: {command}")

if __name__ == '__main__':
    main()