import { IRouter, JupyterFrontEnd } from '@jupyterlab/application';
import { URLExt } from '@jupyterlab/coreutils';
import { showErrorMessage } from '@jupyterlab/apputils';
import { i18nStrings } from '../constants/i18n';
import { describeCluster } from '../service/presignedURL';
import { openSelectAssumableRole, openSelectAuthType } from './ConnectClusterUtils';
import { sleep } from '../utils/CommonUtils';
import { FETCH_EMR_ROLES, OPTIONS_TYPE, fetchApiResponse } from '../service';
import { ClusterRowType } from '../constants';

const i18nStringsError = i18nStrings.EmrClustersDeeplinking.errorDialog;

// IRouter pattern could be matched arbitrary number of times.
// This flag is to ensure the plugin is triggered only once during re-direction.
let isPatternMatched = false;

/**
 * Function to attach EMR cluster to a new notebook
 * @param router
 * @param app
 * @returns
 */
const executeAttachClusterToNewNb = async (router: IRouter, app: JupyterFrontEnd) => {
  if (isPatternMatched) {
    return;
  }
  try {
    const { search } = router.current;
    if (!search) {
      await showErrorMessageAsync(i18nStringsError.invalidRequestErrorMessage);
      return;
    }

    app.restored.then(async () => {
      const { clusterId, accountId: clusterAccountId } = URLExt.queryStringToObject(search);

      if (!clusterId) {
        await showErrorMessageAsync(i18nStringsError.invalidRequestErrorMessage);
        return;
      }

      const fetchEmrRolesResponse = await fetchApiResponse(FETCH_EMR_ROLES, OPTIONS_TYPE.POST, undefined);
      if (!fetchEmrRolesResponse || fetchEmrRolesResponse?.error) {
        await showErrorMessageAsync(i18nStrings.Clusters.fetchEmrRolesError);
        return;
      }

      const describeClusterReponse = await describeCluster(clusterId);
      if (!describeClusterReponse || !describeClusterReponse?.cluster) {
        await showErrorMessageAsync(i18nStringsError.invalidClusterErrorMessage);
        return;
      }
      const clusterData: ClusterRowType = describeClusterReponse.cluster;

      // Execute create new notebook command
      const notebookPanel = await app.commands.execute('notebook:create-new');
      await new Promise((resolve) => {
        notebookPanel.sessionContext.kernelChanged.connect((context: any, kernel: unknown) => {
          resolve(kernel);
        });
      });

      // Sleep for 2 sec for the kernel to start up
      await sleep(2000);

      // if connecting cross account cluster, pop up assumable role widget
      if (clusterAccountId) {
        clusterData.clusterAccountId = clusterAccountId;
        openSelectAssumableRole(fetchEmrRolesResponse, app, clusterData);
      } else {
        clusterData.clusterAccountId = fetchEmrRolesResponse.CallerAccountId;
        openSelectAuthType(clusterData, fetchEmrRolesResponse, app);
      }
    });
  } catch (error) {
    await showErrorMessageAsync(i18nStringsError.defaultErrorMessage);
    return;
  } finally {
    isPatternMatched = true;
  }
};

const showErrorMessageAsync = async (message: string) => {
  return showErrorMessage(i18nStringsError.errorTitle, {
    message: message,
  });
};

export { executeAttachClusterToNewNb };
