import requests
import matplotlib.pyplot as plt

def download_and_save_image(image_id):
    response = requests.get("https://source.unsplash.com/random")
    with open("images/test{}.jpg".format(str(image_id)), "wb") as f:
        f.write(response.content)
        f.close()

def plot_bar_graph(y_data,x_data,y_label,x_label,title,plot_file=None):
    x_ids = list(range(len(x_data)))
    width = 0.25
    fig,ax = plt.subplots()
    ax.bar([x - width/2 for x in x_ids],y_data[0],width,label='multithreading')
    ax.bar([x + width/2 for x in x_ids],y_data[1],width,label='multiprocessing')

    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)
    ax.set_xticks(x_ids)
    ax.set_xticklabels([str(x) for x in x_data])
    ax.legend()

    fig.tight_layout()
    if plot_file is not None:
        plt.savefig(plot_file)
    else:
        plt.show()


def clear_queue(queue):
    while not queue.empty():
        queue.get()
