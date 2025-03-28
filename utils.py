import matplotlib.pyplot as plt

ARCANE_PROFILING = [
    {"ARCANE":233410, "CPU":3653},
    {"ARCANE":36799, "CPU":2583},
    {"ARCANE":21469, "CPU":865},
]
CPU_ONLY_PROFILING = [
    {"ARCANE":0, "CPU":1484415},
    {"ARCANE":0, "CPU":125901},
    {"ARCANE":0, "CPU":19449},
]

def plot_results():
    # Combine ARCANE and CPU values for ARCANE_PROFILING
    bar_width = 0.5
    arcane_values = [
        node["ARCANE"] for node in ARCANE_PROFILING
    ]
    cpu_easy_values = [ node["CPU"] for node in ARCANE_PROFILING]
    # Extract CPU-only values from CPU_ONLY_PROFILING
    cpu_only_values = [node["CPU"] for node in CPU_ONLY_PROFILING]

    # Normalize the values
    nodes = range(len(ARCANE_PROFILING))
    fig, ax = plt.subplots(figsize=(10, 3))
    # Plot ARCANE bars
    for n in nodes:
        total_arcane = arcane_values[n] + cpu_easy_values[n]
        arcane_bars = ax.bar(
            n - bar_width / 2,
            arcane_values[n]/total_arcane,
            bar_width,
            color="indianred",
        )

        cpu_arcane_bars = ax.bar(
            n - bar_width / 2,
            cpu_easy_values[n]/total_arcane,
            bar_width,
            bottom=arcane_values[n]/total_arcane,
            color="maroon",
        )

        # Plot CPU-only bars
        cpu_bars = ax.bar(
            n + bar_width / 2,
            cpu_only_values[n]/total_arcane,
            bar_width,
            color="navajowhite",
        )

        ax.text(
            n + bar_width / 2 - 0.1,
            (cpu_only_values[n]/total_arcane)+0.15,
            f'{cpu_only_values[n]/total_arcane:.2f}x',
            ha='left', va='center', color='darkgoldenrod',
            fontweight='bold',
            fontsize=12,
        )

    total_arcane = sum([arcane_values[n] + cpu_easy_values[n] for n in nodes])
    total_cpu_only = sum(cpu_only_values)

    arcane_bars = ax.bar(
        len(nodes) + bar_width / 2,
        total_cpu_only/total_arcane,
        bar_width,
        color="navajowhite",
    )
    cpu_bars = ax.bar(
        len(nodes) - bar_width / 2,
        1,
        bar_width,
        color="indianred",
    )
    # Add an arrow and text to show the improvement
    improvement = total_cpu_only / total_arcane
    x_pos = len(nodes) - bar_width / 2
    ax.annotate(
        '',
        xy=(x_pos, 1), 
        xytext=(x_pos, total_cpu_only/total_arcane),
        arrowprops=dict(arrowstyle='<->', color='black'),
        ha='center', va='center'
    )
    ax.text(
        x_pos - 0.1,
        (total_cpu_only/total_arcane)+0.1,
        f'{improvement:.2f}x',
        ha='left', va='center', color='firebrick',
        fontweight='bold',
        fontsize=12,
    )
    # Add labels and legend
    ax.set_xlabel("Nodes")
    ax.set_ylabel("Latency w.r.t. ARCANE")
    ax.set_title("ARCANE vs CPU-Only Profiling per Node")
    ax.set_xticks([n for n in nodes]+[len(nodes)])
    ax.set_xticklabels([f"Node {n}" for n in nodes]+["Total"])
    plt.legend(handles=[
        plt.Line2D([0], [0], color="indianred", label='ARCANE NMC'),
        plt.Line2D([0], [0], color="maroon", label='ARCANE CPU'),
        plt.Line2D([0], [0], color="navajowhite", label='CPU-Only'),
    ]
    )
    # Show the plot
    # plt.tight_layout()
    plt.show()
