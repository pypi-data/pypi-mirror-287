# FlowPanel

`FlowPanel` is a Python package for creating a customizable graphical user interface (GUI) using `tkinter`. It allows users to configure a panel with various types of input fields and execute a function with multithreading support.

## Features

* Dynamic Input Fields: Supports multiple input types including entry fields, comboboxes, checkboxes, and listboxes.
* Progress Tracking: Provides a progress bar to indicate ongoing operations.
* Messaging System: Appends messages to a text area with color-coding based on the message type.
* Help Functionality: Opens a help window with support for text and PDF files.
* Multithreading: Runs background tasks without freezing the GUI.
* Customizable GUI: Easily adjust the panel title, descriptions, and input fields.

## Installation

To use `FlowPanel`, you need to have Python 3.x installed on your system. Clone the repository or download the package files.

Install the package locally using:

```bash
pip install flow_panel
```

## Usage

Here’s a basic example of how to use the FlowPanel class:

```python
import time
from flow_panel import FlowPanel


def example_run_function(panel: FlowPanel):
    panel.update_progress(0, 10)
    for i in range(10):
        if panel.should_stop or panel.stop_event.is_set():
            panel.append_message("Process stopped by user.")
            break
        time.sleep(1)
        panel.update_progress(i + 1, 10)
        panel.append_message(f"Step pass {i + 1} completed.")
    if not panel.should_stop:
        panel.append_message("Process finished.")


if __name__ == "__main__":
    gui = FlowPanel(
        title_short="Test Panel",
        title_long="Test Panel GUI",
        list_descriptions=["Run a test process", "with multiple steps."],
        list_user_entries=[
            ["Input 1", "entry", True, None],
            ["Input 2", "combobox", False, ["Option 1", "Option 2"]],
            ["Input 3", "checkbox", False, None],
        ],
        run_function=example_run_function,
        help="This is an example help text."
    )
    gui.mainloop()
```

### Parameters

* `title_short` (str): Short title for the window.
* `title_long` (str): Longer, descriptive title for the window.
* `list_descriptions` (list): List of descriptions to display on the panel.
* `list_user_entries` (list): List of user input fields. Each entry is a list containing:
  * Description label
  * Input type (`entry`, `combobox`, `checkbox`, `multiple choice`)
  * Whether the input is required
  * Options for the input field, if applicable
* `run_function` (callable): Function to execute when the "Start" button is pressed.
* `help` (str, optional): Help text or URL to open for assistance.

## Methods

* `update_progress(value: int, max_value: int)`: Updates the progress bar.
* `append_message(message: str, color_code: Dict[str,str], error_tracking: bool):` Appends a message to the text area with color based on the message type.
* `prompt_to_proceed()`: Prompts the user to proceed to the next step.
  
## Contributing

If you’d like to contribute, please fork the repository and submit a pull request with your changes. Make sure to include tests for new features.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
