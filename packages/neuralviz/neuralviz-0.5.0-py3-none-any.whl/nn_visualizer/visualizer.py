import matplotlib.pyplot as plt
import numpy as np
import torch
from IPython.display import display, clear_output
import seaborn as sns
from sklearn.metrics import confusion_matrix
import io
import PIL.Image
from matplotlib.animation import FuncAnimation

__version__ = '0.5.0'

class NNVisualizer:
    def __init__(self, model, data, fig_size=(10, 8)):
        self.model = model
        self.X, self.y = data
        self.figure, self.ax = plt.subplots(figsize=fig_size)
        self.ax.set_title('Neural Network Visualization')
        self.xx, self.yy = self.create_meshgrid()
        self.history = {'loss': [], 'accuracy': []}

    def create_meshgrid(self):
        x_min, x_max = self.X[:, 0].min() - 1, self.X[:, 0].max() + 1
        y_min, y_max = self.X[:, 1].min() - 1, self.X[:, 1].max() + 1
        xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                             np.arange(y_min, y_max, 0.02))
        return xx, yy

    def plot_decision_boundary(self, epoch, loss, accuracy, cmap='RdYlBu'):
        self.ax.clear()

        Z = self.get_decision_boundary()
        
        self.ax.contourf(self.xx, self.yy, Z, alpha=0.8, cmap=cmap)
        
        scatter = self.ax.scatter(self.X[:, 0].numpy(), self.X[:, 1].numpy(), 
                                  c=self.y.squeeze().numpy(), cmap='coolwarm', 
                                  edgecolor='k', s=20)
        
        self.ax.set_xlim(self.xx.min(), self.xx.max())
        self.ax.set_ylim(self.yy.min(), self.yy.max())
        
        self.ax.set_xlabel('Feature 1')
        self.ax.set_ylabel('Feature 2')
        self.ax.set_title(f'Epoch: {epoch+1}, Loss: {loss:.4f}, Accuracy: {accuracy:.4f}')
        
        legend1 = self.ax.legend(*scatter.legend_elements(), loc="upper right", title="Classes")
        self.ax.add_artist(legend1)
        
        clear_output(wait=True)
        display(self.figure)

    def get_decision_boundary(self):
        self.model.eval()
        with torch.no_grad():
            X_grid = torch.FloatTensor(np.c_[self.xx.ravel(), self.yy.ravel()])
            Z = self.model(X_grid).numpy()
        return Z.reshape(self.xx.shape)

    def plot_loss_curve(self):
        plt.figure(figsize=(10, 5))
        plt.plot(self.history['loss'])
        plt.title('Model Loss')
        plt.ylabel('Loss')
        plt.xlabel('Epoch')
        plt.show()

    def plot_accuracy_curve(self):
        plt.figure(figsize=(10, 5))
        plt.plot(self.history['accuracy'])
        plt.title('Model Accuracy')
        plt.ylabel('Accuracy')
        plt.xlabel('Epoch')
        plt.show()

    def plot_confusion_matrix(self, y_true, y_pred):
        cm = confusion_matrix(y_true, y_pred)
        plt.figure(figsize=(10, 8))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
        plt.title('Confusion Matrix')
        plt.ylabel('True Label')
        plt.xlabel('Predicted Label')
        plt.show()

    def update_history(self, loss, accuracy):
        self.history['loss'].append(loss)
        self.history['accuracy'].append(accuracy)

    def save_plot(self, filename):
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        image = PIL.Image.open(buf)
        image.save(filename)
        buf.close()

    def visualize_feature_importance(self, feature_names):
        weights = list(self.model.parameters())[0].detach().numpy()
        importance = np.abs(weights).sum(axis=0)
        plt.figure(figsize=(10, 5))
        plt.bar(feature_names, importance)
        plt.title('Feature Importance')
        plt.xlabel('Features')
        plt.ylabel('Importance')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def compare_models(self, models, model_names):
        plt.figure(figsize=(12, 8))
        for model, name in zip(models, model_names):
            model.eval()
            with torch.no_grad():
                X_grid = torch.FloatTensor(np.c_[self.xx.ravel(), self.yy.ravel()])
                Z = model(X_grid).numpy().reshape(self.xx.shape)
            plt.contourf(self.xx, self.yy, Z, alpha=0.4, cmap='RdYlBu')
        plt.scatter(self.X[:, 0].numpy(), self.X[:, 1].numpy(), c=self.y.squeeze().numpy(), cmap='coolwarm', edgecolor='k', s=20)
        plt.title('Model Comparison')
        plt.xlabel('Feature 1')
        plt.ylabel('Feature 2')
        plt.legend(model_names)
        plt.show()

    def plot_training_progress(self, num_epochs, update_interval=10):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.set_xlim(0, num_epochs)
        ax.set_ylim(0, 1)
        line_loss, = ax.plot([], [], label='Loss')
        line_acc, = ax.plot([], [], label='Accuracy')
        ax.set_xlabel('Epoch')
        ax.set_ylabel('Metric')
        ax.legend()
        
        def init():
            line_loss.set_data([], [])
            line_acc.set_data([], [])
            return line_loss, line_acc

        def update(epoch):
            if epoch % update_interval == 0:
                loss = self.history['loss'][epoch] if epoch < len(self.history['loss']) else 0
                accuracy = self.history['accuracy'][epoch] if epoch < len(self.history['accuracy']) else 0
                line_loss.set_data(range(epoch+1), self.history['loss'][:epoch+1])
                line_acc.set_data(range(epoch+1), self.history['accuracy'][:epoch+1])
                ax.set_title(f'Epoch: {epoch+1}, Loss: {loss:.4f}, Accuracy: {accuracy:.4f}')
                clear_output(wait=True)
                display(fig)
            return line_loss, line_acc

        ani = FuncAnimation(fig, update, frames=range(num_epochs), init_func=init, repeat=False, interval=100)
        plt.show()

    def plot_feature_distribution(self):
        plt.figure(figsize=(10, 5))
        for i in range(self.X.shape[1]):
            sns.histplot(self.X[:, i].numpy(), kde=True, label=f'Feature {i+1}')
        plt.title('Feature Distributions')
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.legend()
        plt.show()

    def plot_learning_rate_schedule(self, scheduler):
        plt.figure(figsize=(10, 5))
        lr_list = []
        for epoch in range(len(scheduler)):
            lr_list.append(scheduler.get_lr())
        plt.plot(range(len(lr_list)), lr_list)
        plt.title('Learning Rate Schedule')
        plt.ylabel('Learning Rate')
        plt.xlabel('Epoch')
        plt.show()