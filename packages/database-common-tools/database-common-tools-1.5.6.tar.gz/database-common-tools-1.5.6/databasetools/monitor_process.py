import time
from multiprocessing import Process

def monitor_processes(LOG, process_list, target_func, stop_event, *args):
    """
    Monitor and restart processes if they are not alive.

    Parameters:
    - process_list: List of Process objects to monitor.
    - target_func: The target function for the processes.
    - stop_event: Event object to signal when to stop monitoring.
    - args: Variable-length argument list to pass to the target function when creating new processes.
    """
    while True:
        for p in process_list:
            if not p.is_alive():
                LOG.error(f'Process {p.name} is not alive. Restarting...')
                # Recreate the process with the same target function and arguments
                new_process = Process(target=target_func, args=args)
                new_process.start()
                # Replace the terminated process with the new process
                process_list[process_list.index(p)] = new_process
        if stop_event.is_set():
            break
        time.sleep(10)
    LOG.info('Monitoring has been stopped.')
