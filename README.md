# Removarr

A fork of autotorrent-remove that is more up-to-date and has more features.

Removarr automatically manages and removes completed torrents based on your own custom rules.
It helps you keep your disk space clean without the need to manually monitor torrent activity.

Removarr works with **qBittorrent**, **Transmission**, and **μTorrent**, and can be customized to match your exact cleanup preferences.

## Features

* Automatically delete torrents based on conditions like seeding time, ratio, or category
* Works with major torrent clients
* Fully configurable through a simple YAML file
* Supports dry-run mode to preview removals
* Easy to automate with system schedulers (e.g., cron)

## Requirements

* Python 3.6 or newer
* Installed and running torrent client (qBittorrent, Transmission, or μTorrent)

## Installation

Clone this repository and install locally:

```bash
git clone https://github.com/flower/removarr.git
cd removarr
python setup.py install
```

## Configuration

Removarr uses a configuration file to define your cleanup strategies.
You can place the configuration file anywhere; by default, it looks for `config.yml` in the current directory.

Example configuration:

```yaml
my_task:
  client: qbittorrent
  host: http://127.0.0.1
  username: admin
  password: adminadmin
  strategies:
    clean_old:
      categories: IPT
      remove: seeding_time > 1209600 or ratio > 1
  delete_data: true
```

In this example, Removarr will delete torrents in the **IPT** category that have been seeding for more than 14 days or have a ratio greater than 1.

## Usage

To run Removarr:

```bash
removarr
```

To preview which torrents would be removed without actually deleting them:

```bash
removarr --view
```

## Scheduling (Optional)

You can automate Removarr to run periodically using `cron`.
For example, to check every 15 minutes:

```bash
crontab -e
```

Then add a line like this (adjust paths as needed):

```bash
*/15 * * * * /usr/bin/removarr --conf=/path/to/config.yml --log=/path/to/logs
```

* `--conf` specifies the configuration file path
* `--log` defines where logs will be stored (directory must exist)

## Contributing

Feedback, feature requests, and bug reports are always welcome.
Please open an issue or pull request on GitHub to contribute.

## License

This project is released under the MIT License.
You are free to use, modify, and distribute it under the same terms.
