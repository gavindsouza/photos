## Photos

AI Powered Facial Recognition & Photos Clustering (like Google Photos) for your Frappe sites.

[![Try on Frappe Cloud](https://github.com/gavindsouza/photos/raw/main/.github/assets/try-on-fc.png)](https://frappecloud.com/marketplace/apps/photos?referrer=a6d8da54)

#### Demo

<video src="https://user-images.githubusercontent.com/36654812/199225140-0790b589-6d0d-4f34-b45d-294b0b061831.mp4" data-canonical-src="https://user-images.githubusercontent.com/36654812/199225140-0790b589-6d0d-4f34-b45d-294b0b061831.mp4" style="max-height:480px; min-height: 200px; width: -webkit-fill-available;" controls muted>
</video>

Clone the repo and run `docker compose up` in the demo folder to spin up a demo instance :)

#### Usage

You may follow these steps to try out Photos:

1. Login to Desk
1. Upload a new Image file
1. Navigate to the latest Photo Document
1. Scroll down to see the human faces detected
1. Click on each face to show label & more information
1. If label is not set for a given ROI, add it

Photos gets better the more images you store and the more people you label. It may make a few mistakes guessing the names of the people, but it gets better with more data!

#### Installation

Installation is pretty straightforward **IF** you're accustomed to [Frappe](https://frappeframework.com)  Apps:

1. `bench get-app https://github.com/gavindsouza/photos`
1. `bench --site photos-site install-app photos`

If you don't know that and still want to try it out, here's the Frappe documentation for the same - https://frappeframework.com/docs/v14/user/en/installation.

#### More Information

This project consists of:

- Photos: A Frappe App that contains the backend logic & Admin views
- Gallery: A Vue 3 App that contains the tailored gallery UI _[WIP]_

#### Motivation

The initial inspiration for this project was to be an `Open Source Alternative to Google Photos`. However, I've only been able to make a week's time for this in 2 years. If you're seriously looking for an open source alternative to Google Photos, I'd recommend https://photoprism.app/ which is everyting I wanted to build when I thought of doing this back in 2018 ^_^

#### License

[MIT](LICENSE)
