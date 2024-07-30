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
        title_short="Simple Panel",
        title_long="Simple Flow Panel",
        list_descriptions=["Run a test process", "with multiple steps."],
        list_user_entries=[
            ["Input 1", "entry", True, None],
            ["Input 2", "combobox", False, ["Option 1", "Option 2"]],
            ["Input 3", "checkbox", False, None],
        ],
        run_function=example_run_function,
        help="This is a simple example of a flow panel.",
    )
    gui.mainloop()
