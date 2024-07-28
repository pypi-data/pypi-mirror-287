import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

/**
 * Initialization data for the jupyterlab-hello extension.
 */
const plugin: JupyterFrontEndPlugin<void> = {
  id: 'jupyterlab-hello:plugin',
  description: 'A JupyterLab extension.',
  autoStart: true,
  activate: (app: JupyterFrontEnd) => {
    console.log('JupyterLab extension jupyterlab-hello is activated!');
  }
};

export default plugin;
