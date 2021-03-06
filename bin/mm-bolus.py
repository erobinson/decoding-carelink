#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK
from decocare import commands
from decocare.helpers import cli

class BolusApp (cli.CommandApp):
  """ %(prog)s - Send bolus command to a pump.

  XXX: Be careful please.

  Units might be wrong.  Keep disconnected from pump until you trust it by
  observing the right amount first.
  """
  def customize_parser (self, parser):

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--515',
                        dest='strokes_per_unit', action='store_const',
                        const=10
                      )
    group.add_argument('--strokes',
                        dest='strokes_per_unit',
                        type=int
                      )
    parser.add_argument('--units',
                        type=float,
                        help="Amount of insulin to bolus. [default: %(default)s)]"
                        )

    return parser
  def main (self, args):
    print args
    self.bolus(args);

  def bolus (self, args):
    query = commands.Bolus
    kwds = dict(params=[fmt_params(args)])

    resp = self.exec_request(self.pump, query, args=kwds,
                 dryrun=args.dryrun, render_hexdump=False)
    return resp

def fmt_params (args):
  return int(float(args.units) * args.strokes_per_unit)

if __name__ == '__main__':
  app = BolusApp( )
  app.run(None)
