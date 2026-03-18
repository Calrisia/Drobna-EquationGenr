import matplotlib.pyplot as plt
import io
import base64

def latex_to_png(formula: str, fontsize=7):
    """
    Convert LaTeX formula to base64 PNG for embedding in HTML.
    """
    fig, ax = plt.subplots(figsize=(4, 0.6), constrained_layout=True)
    ax.text(
        0.5, 0.5,
        f"${formula}$",
        fontsize=fontsize,
        ha='center',
        va='center'
    )
    ax.axis('off')

    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=250, bbox_inches='tight', transparent=True)
    plt.close(fig)
    buf.seek(0)

    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    return f"data:image/png;base64,{img_base64}"


def latex_to_png_eq(formula: str, fontsize=7):
    """
    Convert LaTeX formula to base64 PNG for embedding in HTML.
    """
    fig, ax = plt.subplots(figsize=(4, 0.6), constrained_layout=True)
    ax.text(
        0.5, 0.5,
        f"${formula}$",
        fontsize=fontsize,
        ha='center',
        va='center'
    )
    ax.axis('off')

    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=250, bbox_inches='tight', transparent=True)
    plt.close(fig)
    buf.seek(0)

    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    return f"data:image/png;base64,{img_base64}"