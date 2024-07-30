import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
from typing import Dict
import webbrowser
import subprocess


class FlowPanel(tk.Tk):

    __title_short: str = "ENTER YOUR TITLE"
    __title_long = "ENTER YOUR LONGER TITLE"
    __list_descriptions = ["Description 1", "Description 2"]
    __list_user_entries = [
        ["Input 1", "entry", True, None],
        ["Input 2", "combobox", False, ["Option 1", "Option 2"]],
        ["Input 3", "checkbox", False, None],
    ]

    def __init__(self, title_short: str, title_long: str, list_descriptions: list, list_user_entries: list, run_function: callable, help: str = None):
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", self.__on_close)
        self.minsize(400, 400)

        self.__title_short = title_short
        self.__title_long = title_long
        self.__list_descriptions = list_descriptions
        self.__list_user_entries = list_user_entries

        self.run_function = run_function
        self.entries = {}
        self.help = help
        self.has_errors = False  # Flag to track errors
        self.confirm_to_proceed = threading.Event()  # Event for confirming to proceed
        self.popup_open = False  # Flag to track if the popup is open
        self.should_stop = False  # Flag to indicate if the process should stop
        self.stop_event = threading.Event()  # Event to signal threads to stop
        self.process_thread = None  # Thread handling the running process

        self.title(self.__title_short)
        self.__create_widgets()

    def __open_help(self):
        if self.help.startswith("http"):
            webbrowser.open(self.help)
        elif self.help.endswith(".pdf"):
            self.__open_pdf(self.help)
        else:
            self.__show_text_help(self.help)

    def __show_text_help(self, help_text: str):
        help_window = tk.Toplevel(self)
        help_window.title("Help")
        text_area = scrolledtext.ScrolledText(help_window, wrap=tk.WORD)
        text_area.insert(tk.END, help_text)
        text_area.config(state=tk.DISABLED)
        text_area.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    def __open_pdf(self, pdf_path: str):
        try:
            subprocess.run(["open", pdf_path], check=True)  # macOS
        except Exception:
            try:
                subprocess.run(["xdg-open", pdf_path], check=True)  # Linux
            except Exception:
                try:
                    subprocess.run(["start", pdf_path],
                                   check=True, shell=True)  # Windows
                except Exception as e:
                    messagebox.showerror("Error", f"Could not open PDF: {e}")

    def __create_widgets(self):
        title_frame = tk.Frame(self)
        title_frame.pack(fill=tk.X, expand=True, pady=10)
        title_label = tk.Label(title_frame, text=self.__title_long, font=(
            "Helvetica", 16), anchor=tk.CENTER)
        title_label.pack(side=tk.LEFT, fill=tk.X, expand=True)
        help_button = tk.Button(title_frame, text="Help",
                                command=self.__open_help)
        help_button.pack(side=tk.RIGHT, padx=10)

        for description in self.__list_descriptions:
            label = tk.Label(self, text=description, font=("Helvetica", 12))
            label.pack(pady=5)

        for user_entry in self.__list_user_entries:
            frame = tk.Frame(self)
            label = tk.Label(
                frame, text=user_entry[0] + (" *" if user_entry[2] else ""), font=("Helvetica", 12))
            label.pack(side=tk.LEFT, padx=5)

            input_type = user_entry[1]
            if input_type == 'entry':
                entry = tk.Entry(frame)
            elif input_type == 'combobox':
                entry = ttk.Combobox(frame, values=user_entry[3])
            elif input_type == 'checkbox':
                entry = tk.Checkbutton(frame)
            elif input_type == 'multiple choice':
                entry = tk.Listbox(frame, selectmode=tk.MULTIPLE)
                for option in user_entry[3]:
                    entry.insert(tk.END, option)
            else:
                raise ValueError("Unsupported input type: " + input_type)

            entry.pack(side=tk.LEFT, padx=5)
            frame.pack(pady=5)

            self.entries[user_entry[0]] = (entry, user_entry[2])

        button_frame = tk.Frame(self)
        self.start_button = tk.Button(
            button_frame, text="Start", command=self.__start)
        self.start_button.pack(side=tk.LEFT, padx=5)
        self.stop_button = tk.Button(
            button_frame, text="Stop", state=tk.DISABLED, command=self.__stop)
        self.stop_button.pack(side=tk.LEFT, padx=5)
        button_frame.pack(pady=10)

        progress_frame = tk.Frame(self)
        progress_label = tk.Label(
            progress_frame, text="Progress: ", font=("Helvetica", 12))
        progress_label.pack(side=tk.LEFT, padx=5)
        self.progress = ttk.Progressbar(
            progress_frame, orient="horizontal", mode="determinate")
        self.progress.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        progress_frame.pack(pady=10, fill=tk.X)

        self.text_area = scrolledtext.ScrolledText(
            self, height=10, wrap=tk.WORD)
        self.text_area.pack(pady=10, fill=tk.BOTH, expand=True)

    def __start(self):
        user_inputs = {}
        for label, (entry, is_required) in self.entries.items():
            value = entry.get() if isinstance(entry, tk.Entry) else entry.get(
            ) if isinstance(entry, ttk.Combobox) else entry.cget("text")
            if is_required and not value:
                messagebox.showwarning("Warning", f"'{label}' is required!")
                return
            user_inputs[label] = value

        confirm = messagebox.askyesno("Confirm", "Are the values correct?")
        if not confirm:
            return

        self.__disable_inputs()
        self.text_area.delete(1.0, tk.END)

        self.should_stop = False
        self.stop_event.clear()
        self.process_thread = threading.Thread(target=self.__run_in_thread)
        self.process_thread.start()

    def __run_in_thread(self):
        self.run_function(self)
        # Schedule GUI updates to happen in the main thread
        self.after(0, self.__enable_inputs_after_thread)

    def __stop(self):
        self.should_stop = True
        self.stop_event.set()
        # Disable stop button immediately
        self.stop_button.config(state=tk.DISABLED)

    def __disable_inputs(self):
        for entry, _ in self.entries.values():
            entry.config(state=tk.DISABLED)
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

    def __enable_inputs(self):
        for entry, _ in self.entries.values():
            entry.config(state=tk.NORMAL)
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def __enable_inputs_after_thread(self):
        if self.process_thread and self.process_thread.is_alive():
            self.process_thread.join()  # Wait for the thread to finish
        self.__enable_inputs()

    def update_progress(self, value: int, max_value: int):
        """ Updates the progress bar.
        @param value: The current value.
        @param max_value: The maximum value.
        """
        self.after(0, self.__update_progress, value, max_value)

    def __update_progress(self, value: int, max_value: int):
        """ Helper method to update the progress bar safely. """
        self.progress["value"] = value
        self.progress["maximum"] = max_value

    def append_message(self, message: str, color_code: Dict[str, str] = {"warning": "orange", "error": "red", "pass": "green", "fail": "red"}, error_tracking: bool = True):
        """ Appends a message to the text area with color based on the message type (case-insensitive):
        @param message: The message to append.
        @param color_code: A dictionary of message types and their corresponding colors.
        @param error_tracking: A flag to track if the message is an error.
        """
        def update_text_area():
            color = "black"
            for key, value in color_code.items():
                if key in message.lower():
                    color = value
                    break
                if error_tracking and key in message.lower():
                    self.has_errors = True

            tag = f"tag_{self.text_area.index(tk.END)}"
            self.text_area.insert(tk.END, message + "\n", (tag,))
            self.text_area.tag_config(tag, foreground=color)
            self.text_area.see(tk.END)

        self.after(0, update_text_area)

    def __show_completion_popup(self):
        self.after(0, self.__show_popup)

    def __show_popup(self):
        if self.has_errors:
            messagebox.showerror("Completion Status",
                                 "Process completed with errors/failures.")
        else:
            messagebox.showinfo(
                "Completion Status", "Process completed successfully without failures.")
        self.has_errors = False  # Reset the flag

    def confirm_proceed(self):
        def proceed():
            self.confirm_to_proceed.set()
            self.popup_open = False
            popup.destroy()

        def exit_process():
            self.confirm_to_proceed.clear()
            self.append_message("Process exited by user.")
            self.after(0, self.__enable_inputs_after_thread)
            self.popup_open = False
            popup.destroy()

        self.confirm_to_proceed.clear()
        self.popup_open = True

        popup = tk.Toplevel(self)
        popup.geometry("300x100")
        popup.resizable(False, False)
        popup.title("Proceed Confirmation")
        label = tk.Label(
            popup, text="Do you want to proceed to the next step?")
        label.pack(pady=10)
        button_frame = tk.Frame(popup)
        yes_button = tk.Button(button_frame, text="Yes", command=proceed)
        yes_button.pack(side=tk.LEFT, padx=5)
        no_button = tk.Button(button_frame, text="No", command=exit_process)
        no_button.pack(side=tk.LEFT, padx=5)
        button_frame.pack(pady=10)

        self.stop_button.config(state=tk.DISABLED)
        popup.protocol("WM_DELETE_WINDOW", exit_process)
        self.confirm_to_proceed.wait()
        self.stop_button.config(state=tk.NORMAL)

    def __on_close(self):
        if self.process_thread and self.process_thread.is_alive():
            messagebox.showwarning(
                "Warning", "Please use the stop button to stop the process before closing the application.")
        else:
            self.__destroy()

    def __destroy(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.stop_event.set()  # Signal threads to stop
            self.quit()  # Properly quit Tkinter main loop
            self.destroy()  # Destroy the main window


def dummy_run_function(flow_panel_instance):
    import time
    for i in range(10):
        if flow_panel_instance.should_stop:
            break
        time.sleep(1)
        flow_panel_instance.update_progress(i + 1, 10)
        flow_panel_instance.append_message(f"Step {i+1} completed.", {
                                           "warning": "orange", "error": "red", "pass": "green", "fail": "red"}, error_tracking=True)
    flow_panel_instance.__show_completion_popup()


if __name__ == "__main__":
    app = FlowPanel(
        title_short="Short Title",
        title_long="This is the Long Title",
        list_descriptions=["Description 1", "Description 2"],
        list_user_entries=[
            ["Input 1", "entry", True, None],
            ["Input 2", "combobox", False, ["Option 1", "Option 2"]],
            ["Input 3", "checkbox", False, None]
        ],
        run_function=dummy_run_function,
        help="This is a help text."
    )
    app.mainloop()
