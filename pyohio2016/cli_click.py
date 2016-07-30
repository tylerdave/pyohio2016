#!/usr/bin/env python

import click
import sys
from pyohio2016 import counter


@click.command()
@click.argument('infile', type=click.File('r'), default='-')
@click.argument('outfile', type=click.File('w'), default='-')
@click.option('--log-file', '-l', type=click.File('w'), default=sys.stderr)
@click.option('--verbose', '-v', is_flag=True)
def cli(infile, outfile, log_file, verbose):
    """ Count the occurances of characters in INFILE and output to OUTFILE. """

    if verbose:
        click.echo("Infile: {0}".format(infile), file=log_file)
        click.echo("Outfile: {0}".format(outfile), file=log_file)

    text = infile.read()
    char_counts = counter.count_chars(text)
    output = "\n".join(["{0} {1}".format(k, v) for k, v in char_counts])
    click.echo("Counted characters...", file=log_file)
    click.secho(output, file=outfile, fg='green')

    if verbose:
        click.echo("Done.".format(outfile), file=log_file)


if __name__ == '__main__':
    cli()
