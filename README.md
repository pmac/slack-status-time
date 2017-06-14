# Slack Status Time

Automatically update your slack status with the current time in your timezone.

This isn't probably all that useful, but I enjoyed making it. It will update your Slack status
to your local hour, and set the status emoji to that hour's clock face.

## Usage

Best way to go is to use Docker. It's all set to go. You just need to generate a Slack token
at their [API legacy token page](https://api.slack.com/custom-integrations/legacy-tokens), and
then pass that in as an the argument to the `run-update` script.

```bash
$ ./run-update xoxp-XXXXXXXX-XXXXXXXX...
```

The default timezone for the script is "America/New_York", but you can set any other by setting the `TZ`
environment variable:

```bash
$ TZ="America/Los_Angeles" ./run-update xoxp-XXXXXXXX-XXXXXXXX...
```

The script will build the docker image and run the script.

Enjoy!
