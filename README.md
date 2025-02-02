<div align="center">
  <a href="#">
  <img src="https://raw.githubusercontent.com/noppanut15/depthviz/main/assets/logo/depthviz-temp-logo.png" width="300" alt="depthviz logo"/>
  </a>
  <a name="readme-top"></a>

*A CLI tool that creates heads-up displays <br>for your **freediving videos**, <br>automatically tracking **depth** and **time** <br>from your **dive computer logs** or **manual input**.*

[![PyPI - Version][version_badge_img]][version_badge_url] [![GitHub Actions Workflow Status][build_badge_img]][build_badge_url] [![Coveralls][coverage_badge_img]][coverage_badge_url] [![PyPI - Status][pypi_status_img]][pypi_status_url] [![PyPI Downloads][download_badge_img]][download_badge_url]

**&searr;&nbsp;&nbsp;Quick Links&nbsp;&nbsp;&swarr;**

[Features](#-features) • [Installation](#️-installation) • [Usage](#-usage) • [No Dive Computer?](#-no-dive-computer) • [How It Works](#-how-it-works) • [Contribution](#-contribution) • [License](#️-license) • [Contact](#-contact)

**&searr;&nbsp;&nbsp;Share the project's link to your friends&nbsp;&nbsp;&swarr;**

[![Share on X][x_share_img]][x_share_url] [![Share on Facebook][facebook_share_img]][facebook_share_url] [![Share on Telegram][telegram_share_img]][telegram_share_url] [![Share on WhatsApp][whatsapp_share_img]][whatsapp_share_url] [![Share on Reddit][reddit_share_img]][reddit_share_url]
</div>

![depthviz DEMO](https://raw.githubusercontent.com/noppanut15/depthviz/main/assets/demo-compressed-v2.gif)

---
## ✨ Features

<img src="https://raw.githubusercontent.com/noppanut15/depthviz/main/assets/final-video-showcase-400x400.gif" alt="showcase video" align="right" width="385px" />
 
Why use *depthviz*?

- **Free & Open-Source** – Made for all freedivers, whether or not you have a dive computer.
- **Cross-Platform** – Works on **Windows**, **macOS**, and **Linux**.
- **Multi-Source Dive Log Support:** Works with dive logs from **Apnealizer, Shearwater, Garmin, Suunto**, or even your own **manual input**.
- **Customizable Display** – Control decimal places, fonts, colors, stroke width, etc.
- **Easy Video Integration** – Use your favorite editor (CapCut, etc.) with generated overlays.
- **Smooth Depth Display** – Automatically fills in missing data for a seamless and natural depth display. Includes *zero-based* depth mode to smoothly estimates a 0m start if your dive log starts underwater.

> [!TIP]
> Perfect for performance freedivers tracking PBs or analyzing technique. Overlay your data and see every moment of your dive!

<div align="right">

[&nwarr; Back to top](#readme-top)

</div>

---

## 🌟 Like depthviz?

If you like `depthviz` and find it useful, please give it a shiny [![star](https://img.shields.io/github/stars/noppanut15/depthviz
)](https://github.com/noppanut15/depthviz) ✨

Want **early access** to new open-source projects, exclusive insights, and sneak peeks into upcoming `depthviz` features? 🚀

<a href="https://github.com/noppanut15/" title="Follow Me on GitHub"><picture><source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/follow%20me%20on%20github-white.svg?style=for-the-badge&logo=github&logoColor=black"><img src="https://img.shields.io/badge/follow%20me%20on%20github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white" title="Follow Me on GitHub" /></picture></a>

I’d also love to see your diving stories or videos made with `depthviz`! Share your creations by tagging me [@noppanut15](https://www.instagram.com/noppanut15/) or using the hashtag **#depthviz**. 

See you in the deep! 🌊😊

<div align="right">

[&nwarr; Back to top](#readme-top)

</div>

## 🛠️ Installation
### Prerequisites
- **Python 3.9 or higher**  
  [Download Python](https://www.python.org/downloads/) • [How to install Python](https://realpython.com/installing-python/)
- **pipx** – the recommended tool for installing Python CLI tools  
  [How to install pipx](https://pipx.pypa.io/stable/installation/)

### Install depthviz

Open your terminal and run:
```bash
pipx install depthviz
```

### Upgrade

When a new version is available, update with:

```bash
pipx upgrade depthviz
```

Check your installed version with:
```bash
depthviz --version
```

<div align="right">

[&nwarr; Back to top](#readme-top)

</div>

## 🚀 Usage

`depthviz` turns your dive logs into overlay videos that show your depth and elapsed time. Follow these 3 simple steps: 🏊‍♂️🎥

### Step 1: Prepare Your Dive Data

- **✅ With a Dive Computer:**<br>Export your dive log from your dive computer or diving application. (see [Supported Dive Log Formats](#-supported-dive-log-formats) below).
- **🚫 No Dive Computer?**<br>You can record your dive manually (details in [No Dive Computer?](#-no-dive-computer)).


### Step 2: Generate the Overlay 🎬

Run this command to create your depth overlay video from your dive log:

```bash
depthviz -i YOUR_DIVE_LOG -s DATA_SOURCE -o OUTPUT_VIDEO.mp4
```
**Example (Garmin dive log):**
```bash
depthviz -i 123456_ACTIVITY.fit -s garmin -o my_dive_overlay.mp4
```
| &nbsp;&nbsp;&nbsp;&nbsp;Option&nbsp;&nbsp;&nbsp;&nbsp; | Short | Values                                                               | Description                                                                                           |
| ------------------------------------------------------ | :---: | -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `--input`                                              | `-i`  | File path                                                            | Path or filename to your dive log file.                                                               |
| `--source`                                             | `-s`  | `apnealizer`,<br>`shearwater`,<br>`garmin`,<br>`suunto`,<br>`manual` | The data source.<br>(See the [Supported Dive Log Formats](#-supported-dive-log-formats) for details.) |
| `--output`                                             | `-o`  | File path                                                            | Path or filename for the output video. (must end with `.mp4`)                                         |

#### 📂 Supported Dive Log Formats

|    Source    | Description                                                                                                                                                                                                                                                   | File type |
| :----------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------: |
| `apnealizer` | Exported logs from the **Apnealizer** app. <br> [![Get log][get_log_img]](https://apnealizer.com/)                                                                                                                                                            |    CSV    |
| `shearwater` | Logs from **Shearwater** dive computers. <br> [![Get log][get_log_img]](https://shearwater.com/pages/shearwater-cloud)                                                                                                                                        |    XML    |
|   `garmin`   | Logs from **Garmin** dive computers. <br> [![Get log][get_log_img]](https://connect.garmin.com/signin/) [![How to][how_to_img]](https://github.com/noppanut15/depthviz/blob/main/docs/GARMIN.md)                                                              |    FIT    |
|   `suunto`   | Logs from **Suunto** dive computers. <br> [![Get log][get_log_img]](https://www.suunto.com/suunto-app/suunto-app-2022/)  [![How to][how_to_img]](https://www.suunto.com/Support/faq-articles/suunto-app/what-type-of-files-can-i-export-from-the-suunto-app/) |    FIT    |
|   `manual`   | Manually entered depth logs. <br> [![How to][how_to_img]](#-no-dive-computer)                                                                                                                                                                                 |    CSV    |


#### 🎛 Advanced Customization Options
Want more control? Use these optional parameters:
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Option&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Values&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |                           Default                           | Description                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------: | :---------------------------------------------------------: | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `-d` or <br/>`--decimal-places`                                                                                                                                    |                                `0`, `1`, or `2`                                |                             `0`                             | Number of decimal places in the depth overlay.                                                                                            |
| `--depth-mode`                                                                                                                                                     |                         `raw` <br/>or<br/>`zero-based`                         |                            `raw`                            | `raw` shows the actual depth; `zero-based` forces the overlay to start/end at 0m. [See Raw vs Zero-Based](#-raw-vs-zero-based-depth-mode) |
| `--no-minus`                                                                                                                                                       |                                       -                                        |                              -                              | Removes the minus sign from depth values (e.g., `10m` instead of `-10m`).                                                                 |
| `--font`                                                                                                                                                           |                                   File path                                    | [Default font](https://fonts.google.com/specimen/Open+Sans) | Path to a custom font file for the text.                                                                                                  |
| `--bg-color`                                                                                                                                                       |                             Color name or hex code                             |                           `black`                           | Background color (e.g., `green`, `'#000000'`).                                                                                            |
| `--stroke-width`                                                                                                                                                   |                                Positive integer                                |                             `5`                             | Thickness of the text outline for better visibility.                                                                                      |


<details><summary><strong>Example Command with Advanced Options</strong></summary><br>

Example of generating a depth overlay video named `mydive.mp4` using data from `123456_ACTIVITY.fit` exported from [Garmin Connect](https://github.com/noppanut15/depthviz/blob/main/docs/GARMIN.md):

```bash
depthviz \
    -i 123456_ACTIVITY.fit -s garmin -o mydive.mp4 \
    --depth-mode zero-based \
    --decimal-places 1 \
    --no-minus \
    --bg-color green \
    --font ~/Downloads/YourCustomFont.ttf
```

- Set the depth display mode to **zero-based** to adjust the depth to start and end at 0m. (Learn more about [Zero-Based Depth Mode](#-raw-vs-zero-based-depth-mode))
- The depth values will be displayed with **one** decimal place.
- The minus sign will be **hidden**.
- The background color will be set to **green** for chroma keying.
- A **custom font** file at `~/Downloads/YourCustomFont.ttf` will be used for the text.

---
</details>
<br>

<p align="center"><img src="https://raw.githubusercontent.com/noppanut15/depthviz/main/assets/depth-decimal-places-5s-trimmed.gif" width="600px" alt="decimal places comparison"/></p>

> [!TIP]
> Use the `--decimal-places` option to control the precision of the depth display (e.g., `--decimal-places 1` displays depths like `-12.5m`)

#### Time Overlay Video

<p align="center"><img src="https://raw.githubusercontent.com/noppanut15/depthviz/main/assets/time-overlays.gif" alt="time overlay demo" width="600px"/></p>

You can also generate a time overlay video as a separate video that displays the time elapsed during the dive. It will be exported in the same directory as the depth overlay video.

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Option&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Values | Description                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------ | ---------------------------- |
| `--time`                                                                                                                                               | -      | Create a time overlay video. |

<details><summary><strong>Example Command with Time Overlay</strong></summary><br>

Example of generating a depth overlay video named `mydive.mp4` and a time overlay video by adding the `--time` option:

```bash
depthviz -i 123456_ACTIVITY.fit -s garmin -o mydive.mp4 --time
```
> The time overlay video will be automatically generated and saved in the same directory as the depth overlay video with the filename `mydive_time.mp4`.

</details>


### Step 3: Integrate with Your Footage

<p align="center"><picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/noppanut15/depthviz/main/assets/step3-dark-v2.jpeg" width="500px"><img src="https://raw.githubusercontent.com/noppanut15/depthviz/main/assets/step3-light-v2.jpeg" width="500px" title="integrate overlays with your footage" /></picture></p> 

Import the generated **depth overlay** and **time overlay** (if used) into your video editing software. Remove the background color. Adjust position of the overlays to suit your video style.

> [🎓 Watch a quick tutorial](https://www.youtube.com/watch?v=ZggKrWk98Ag): How to import overlays in CapCut.

> [!TIP]
> **🎨 Chroma Keying**: If you want to remove the background color from the overlay, use the [chroma key](https://en.wikipedia.org/wiki/Chroma_key) effect in your video editor. You can use the `--bg-color` option to set the background color to match your video editor's chroma key color. Using `--bg-color green` is a common choice.

<div align="right">

[&nwarr; Back to top](#readme-top)

</div>

## 🚫 No Dive Computer?

Even without a dive computer, **you can** create a depth overlay! Simply record **key moments** of your dive (using depth markers on your rope, for example) and prepare a CSV file with two columns:
- **Time**: in seconds
- **Depth**: in meters

**Example Manual Input File:**

| Time  | Depth |
| :---: | :---: |
|   0   |   0   |
|   6   |   5   |
|  12   |  10   |
|  19   |  15   |
|  26   |  10   |
|  33   |   5   |
|  39   |   0   |

[![Download Input File](https://img.shields.io/badge/Download%20Input%20File-1974D2?style=for-the-badge&logo=readdotcv)](https://github.com/noppanut15/depthviz/blob/main/assets/manual-input-example.csv)

**Example Command**:
```bash
depthviz -i manual_input.csv -s manual -o output_video.mp4
```

> [!TIP]
> For a simple dive, recording just three points (start, maximum depth, end) is enough. `depthviz` will interpolate the values for a smooth depth profile!

> [!IMPORTANT]
> For more complex dives (e.g., dives with significant variations in descent/ascent rate or bottom time), more data points are recommended.

<a href="https://2bfreeequipment.com/shop/2-b-free-freediving-rope-superstatic-marked-with-stopper/"><p align="center"><img src="https://raw.githubusercontent.com/noppanut15/depthviz/main/assets/marked-rope-example.png" alt="Example of a Freediving Rope with Depth Markers" width="600px"/></p></a>
> [!TIP]
> Freediving rope with depth markers can help you record key moments of your dive.

<div align="right">

[&nwarr; Back to top](#readme-top)

</div>

## 💡 Raw vs Zero-Based Depth Mode

<p align="center"><img src="https://raw.githubusercontent.com/noppanut15/depthviz/main/assets/depth-mode-comparison.jpg" alt="Depth Mode: raw vs zero-based" width="600px"/></p>

`depthviz` offers **two ways** to display depth:

|       Mode        | Best For                 | Description                                                                                                                                               |
| :---------------: | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `raw` *(Default)* | Accuracy, Dive Analysis  | Shows **actual recorded** depth. Your dive might start at **-0.3m, -0.5m, etc.** if the dive computer didn’t record at the surface. *(left figure)*       |
|   `zero-based`    | Aesthetic Video Overlays | Adjusts depth to **start and end at 0m** for a smoother display. Assumes a **1m/s descent/ascent rate** for the missing surface portion. *(right figure)* |

> [!TIP]
> - Use `raw`  mode if accuracy matters (e.g., dive analysis).  
> - Use `zero-based` if your dive log starts/ends underwater but you want a clean 0m start/end. (e.g., social media videos)

<div align="right">

[&nwarr; Back to top](#readme-top)

</div>

## 🧠 How It Works

`depthviz` transforms your dive log data into an overlay video that visually tracks your depth in real time. It supports multiple dive computer formats and even allows manual data input, making it a versatile tool for freedivers looking to analyze and improve their performance.

### 🔬 Understanding Depth Calculation
Dive computers record either **depth** directly or **pressure**, which `depthviz` converts into depth using fluid statics principles. Understanding this process helps ensure accurate depth visualization.

#### 📌 Step 1: Calculating Hydrostatic Pressure

Underwater pressure consists of atmospheric pressure (collected during the surface interval or dive start) and hydrostatic pressure. To determine hydrostatic pressure:

<br><p align="center"><picture><source media="(prefers-color-scheme: dark)" srcset="https://latex.codecogs.com/svg.image?\large&space;{\color{White}P_{\text{hydro}}=P_{\text{absolute}}-P_{\text{atmospheric}}}"><img src="https://latex.codecogs.com/svg.image?\large&space;$$P_{\text{hydro}}=P_{\text{absolute}}-P_{\text{atmospheric}}$$" title="$$P_{\text{hydro}}=P_{\text{absolute}}-P_{\text{atmospheric}}$$" /></picture></p><br>

<!-- $$
P_{\text{hydro}} = P_{\text{absolute}} - P_{\text{atmospheric}}
$$ -->

Hydrostatic pressure increases with depth due to the weight of the water above, making it a key factor in depth calculations.

#### 📌 Step 2: Converting Pressure to Depth

Once hydrostatic pressure is known, depth can be calculated using the formula:

<br><p align="center"><picture><source media="(prefers-color-scheme: dark)" srcset="https://latex.codecogs.com/svg.image?\large&space;{\color{White}h=\frac{P_{\text{hydro}}}{\rho&space;g}}"><img src="https://latex.codecogs.com/svg.image?\large&space;$$h=\frac{P_{\text{hydro}}}{\rho&space;g}$$" title="$$h=\frac{P_{\text{hydro}}}{\rho&space;g}$$" /></picture></p>

<!-- $$
h=\frac{P_{\text{hydro}}}{\rho g}
$$ -->

Where:

- **h** = Depth in meters
- **ρ** = Water density *(EN13319 standard: 1019.7 kg/m³, standard for dive computers)*
- **g** = Gravity (9.80665 m/s²)

> [!NOTE]
> Water density varies between saltwater and freshwater, which can affect depth accuracy. Custom density settings are planned for future updates.

### 📊 Handling Missing Data

Dive computers record data at different rates, which may result in **gaps in data** due to device limitations, battery-saving settings, or inconsistent logging intervals. To create a smooth depth profile, `depthviz` applies [Linear Interpolation](https://en.wikipedia.org/wiki/Linear_interpolation) to estimate missing values.

To estimate missing depth values, `depthviz` uses the following formula:

<br><p align="center"><picture><source media="(prefers-color-scheme: dark)" srcset="https://latex.codecogs.com/svg.image?\large&space;{\color{White}d=d_0+(t-t_0)\frac{d_1-d_0}{t_1-t_0}}"><img src="https://latex.codecogs.com/svg.image?\large&space;$$d=d_0+(t-t_0)\frac{d_1-d_0}{t_1-t_0}$$" title="$$d=d_0+(t-t_0)\frac{d_1-d_0}{t_1-t_0}$$" /></picture></p>

<!-- $$
d=d_0+(t-t_0)\frac{d_1-d_0}{t_1-t_0}
$$ -->

Where:

- **d** = Estimated depth
- **t** = Missing timestamp
- **(t₀, d₀)** and **(t₁, d₁)** = Known data points

This ensures a smooth transition between recorded depth values.

<p align="center">
  <img src="./assets/linear-interpolation-example.png" width="500" alt="Example Chart: Linear Interpolation of Depth Over Time"/>
</p>

> **Example:** If your dive log records 5m at 6s and jumps to 10m at 12s, `depthviz` estimates intermediate depths at 7s, 8s, etc., for a seamless display.


### 🎥 Creating the Overlay Video

Once the data is processed, `depthviz`:

✅ **Smooths depth values**, ensuring natural and fluid transitions between recorded points.<br>✅ **Applies display settings**, including color, font, and stroke width, for full customization.<br>✅ **Generates an overlay video**, ready for integration with your dive footage.

This functionality allows freedivers to analyze their performance, track progress, and create engaging underwater visuals effortlessly. Whether for personal improvement, training analysis, or social media sharing.

<div align="right">

[&nwarr; Back to top](#readme-top)

</div>

## 🌱 Contribution

We welcome contributions to the `depthviz` project! If you have any ideas for improvement, bug fixes, or feature suggestions, feel free to [open an issue](https://github.com/noppanut15/depthviz/issues) to discuss or [submit a pull request](https://github.com/noppanut15/depthviz/pulls).

<div align="right">

[&nwarr; Back to top](#readme-top)

</div>

## ⌚ Help Us Expand Dive Computer Support!

**Missing your dive computer?** Help us add support! If you have a dive computer that is not currently supported by `depthviz`, you can help us by donating a sample dive log file exported from your device. This will allow us to analyze the data format and implement the necessary parsing logic to add support for your device.

To share your dive data, please follow the detailed instructions in our [**Donate My Dive**](https://github.com/noppanut15/depthviz/issues/15) guide.

<div align="right">

[&nwarr; Back to top](#readme-top)

</div>

## ⚖️ License

**depthviz** is free and open-source software licensed under the [Apache License 2.0](https://github.com/noppanut15/depthviz/blob/main/LICENSE), created and supported by [Noppanut Ploywong](https://github.com/noppanut15) with ❤️ for fellow freedivers.

<!-- This project is licensed under the Apache License 2.0. See the [LICENSE](https://github.com/noppanut15/depthviz/blob/main/LICENSE) file for details. -->

<div align="right">

[&nwarr; Back to top](#readme-top)

</div>

## 📦 CycloneDX SBOM

This project provides a CycloneDX Software Bill of Materials (SBOM) in JSON format. The SBOM is generated by the [GitHub Actions workflow](https://github.com/noppanut15/depthviz/blob/main/.github/workflows/deploy.yaml) and is available as an artifact for each release. The SBOM is generated using the [cyclonedx-python](https://github.com/CycloneDX/cyclonedx-python) library.

<div align="right">

[&nwarr; Back to top](#readme-top)

</div>

## 📬 Contact

For any inquiries, please [open an issue](https://github.com/noppanut15/depthviz/issues) or contact the maintainer at [noppanut.connect@gmail.com](mailto:noppanut.connect@gmail.com).

<div align="right">

[&nwarr; Back to top](#readme-top)

</div>

<!-- Badge links -->
[version_badge_img]: https://img.shields.io/pypi/v/depthviz?label=version&logo=pypi&logoColor=white
[build_badge_img]: https://img.shields.io/github/actions/workflow/status/noppanut15/depthviz/deploy.yaml?logo=github
[coverage_badge_img]: https://img.shields.io/coveralls/github/noppanut15/depthviz?logo=coveralls
[pypi_status_img]: https://img.shields.io/pypi/status/depthviz?logo=pypi&logoColor=white
[download_badge_img]: https://static.pepy.tech/badge/depthviz
[version_badge_url]: https://pypi.org/project/depthviz/
[build_badge_url]: https://github.com/noppanut15/depthviz/actions
[coverage_badge_url]: https://coveralls.io/github/noppanut15/depthviz
[pypi_status_url]: https://pypi.org/project/depthviz/
[download_badge_url]: https://pepy.tech/projects/depthviz

<!-- Social links -->
[x_share_url]: https://x.com/intent/tweet?hashtags=depth%2Cfreediving%2Chud&text=A%20CLI%20tool%20that%20creates%20heads-up%20displays%20for%20your%20freediving%20videos%2C%20automatically%20tracking%20depth%20and%20time%20from%20dive%20computer%20logs%20or%20manual%20records.&url=https%3A%2F%2Fgithub.com%2Fnoppanut15%2Fdepthviz
[telegram_share_url]: https://t.me/share/url?url=https%3A//github.com/noppanut15/depthviz&text=A%20CLI%20tool%20that%20creates%20heads-up%20displays%20for%20your%20freediving%20videos,%20automatically%20tracking%20depth%20and%20time%20from%20dive%20computer%20logs%20or%20manual%20records.
[whatsapp_share_url]: https://api.whatsapp.com/send?text=A%20CLI%20tool%20that%20creates%20heads-up%20displays%20for%20your%20freediving%20videos%2C%20automatically%20tracking%20depth%20and%20time%20from%20dive%20computer%20logs%20or%20manual%20records.%20https%3A%2F%2Fgithub.com%2Fnoppanut15%2Fdepthviz
[reddit_share_url]: https://www.reddit.com/submit?url=https%3A%2F%2Fgithub.com%2Fnoppanut15%2Fdepthviz&title=A%20CLI%20tool%20that%20creates%20heads-up%20displays%20for%20your%20freediving%20videos%2C%20automatically%20tracking%20depth%20and%20time%20from%20dive%20computer%20logs%20or%20manual%20records.%20%23depth%20%23freediving
[facebook_share_url]: https://www.facebook.com/sharer/sharer.php?u=https%3A//github.com/noppanut15/depthviz
[x_share_img]: https://img.shields.io/badge/x_(twitter)-black?style=for-the-badge&logo=x
[telegram_share_img]: https://img.shields.io/badge/telegram-black?style=for-the-badge&logo=telegram
[whatsapp_share_img]: https://img.shields.io/badge/whatsapp-black?style=for-the-badge&logo=whatsapp
[reddit_share_img]: https://img.shields.io/badge/reddit-black?style=for-the-badge&logo=reddit
[facebook_share_img]: https://img.shields.io/badge/facebook-black?style=for-the-badge&logo=facebook

<!-- Help -->
[how_to_img]: https://img.shields.io/badge/How%20to-1974D2?style=flat-square&logo=gitbook&logoColor=white
[get_log_img]: https://img.shields.io/badge/Get%20log-1974D2?style=flat-square&logo=transmission&logoColor=white