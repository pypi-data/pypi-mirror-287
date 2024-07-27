import React from 'react';
import {
     CssBaseline,
     Typography,
     MenuItem,
     Select,
     SelectChangeEvent,
     Snackbar,
     TextField,
     Tooltip,
     styled,
     IconButton,
     InputAdornment,
     InputLabel,
     Grid,
     Card,
     CardContent
} from '@mui/material';
import { IoCopyOutline } from 'react-icons/io5';
import copyToSystem from '../common/copyToClipboard';
import { IEndpoint, IEndpoints, IEndpointVersion } from '../common/types';
import { MdDeleteOutline } from "react-icons/md";
import { requestAPI } from '../common/requestAPI';
import { CommonContext } from '../contexts/CommonContext';

type EndpointInfoProps = {
     endpoint: IEndpoint,
     apiBakerDomain: string,
     getEndpoints: () => void
     getSysEnv: () => void
}

const EndpointSummary: React.FC<EndpointInfoProps> = (props): JSX.Element => {
     const { currentUser } = React.useContext(CommonContext) as CommonContextType;
     const [version, setVersion] = React.useState<string>('');
     const [snackbarOpen, setSnackbarOpen] = React.useState<boolean>(false)
     const [endpointURLToCopy, setEndpointURLToCopy] = React.useState('')
     const [versionDescription, setVersionDescription] = React.useState<string>('')
     const [versions, setVersions] = React.useState<IEndpointVersion[]>(props.endpoint.versions)
     // const enpointdVersions = props.endpoint.versions || []

     React.useEffect(() => {
          setVersion(
               `${versions.length > 0 ? versions[0].id : ''
               }`
          );
          setVersionDescription(
               `${versions.length > 0
                    ? versions[0].description
                    : ''
               }`
          );
     }, [props.endpoint.versions]);

     React.useEffect(() => {
          props.getSysEnv()
          setEndpointURLToCopy(
               `${props.apiBakerDomain}/endpoints/${props.endpoint.id}/versions/${version}/submit`
          );
     }, [props.endpoint.id, version, props.apiBakerDomain]);

     const handleVersionChange = (event: SelectChangeEvent) => {
          event.preventDefault();
          console.log(event.target.value);
          setVersion(event.target.value);
          setVersionDescription(versions.find((v) => v.id === event.target.value)?.description ?? "");
     };

     const handleCopyToClipboard = () => {
          try {
               copyToSystem(endpointURLToCopy as string)
               setSnackbarOpen(true)
          } catch (error) {
               console.log(`Error copying to clipboard => ${JSON.stringify(error, null, 2)}`)
          }
     }

     const handleDelete = async (event: React.MouseEvent<SVGElement>) => {
          try {
               event.stopPropagation();
               const versionId = event.currentTarget.id
               await requestAPI<any>("version", {
                    method: "DELETE",
                    body: JSON.stringify({
                         current_user: currentUser,
                         endpoint_id: props.endpoint.id,
                         version_id: versionId,
                    })
               })

               props.getEndpoints()
               const response = await requestAPI<IEndpoints>("endpoint?owner=" + props.endpoint.owner, {
                    method: "GET",
               });
               const responseObj = JSON.parse(response.toString())
               const endpoints = responseObj.data
               const endpoint = endpoints.find((endpoint: IEndpoint) => endpoint.id === props.endpoint.id)
               setVersions(endpoint ? endpoint.versions : [])
          } catch (error) {
               console.log(`Error copying to clipboard => ${JSON.stringify(error, null, 2)}`)
          }
     };

     function DeleteButton({ isSelected, versionId }: { isSelected: boolean, versionId: string }) {
          if (isSelected) {
               return <MdDeleteOutline id={versionId} fontSize="large" onClick={handleDelete} />
          }
          return null
     }

     const IconButtonWithTooltip = styled(IconButton)({
          root: {
               '&.Mui-disabled': {
                    pointerEvents: 'auto',
               },
          },
     });

     const AlignedInputAdornment = styled(InputAdornment)({
          margin: '0 auto', // fix for vertically unaligned icon
     });

     return (
          <React.Fragment>
               <CssBaseline />
               <Card sx={{ maxWidth: '100%' }}>
                    <CardContent>
                         <Grid
                              container
                              direction="column"
                              justifyContent="space-around"
                              alignItems="flex-start"
                         >
                              <Grid item width={'100%'}>
                                   <Grid
                                        container
                                        direction="row"
                                        justifyContent="flex-start"
                                        alignItems="flex-start"
                                   >
                                        <Grid item width={'50%'}>
                                             <Grid
                                                  container
                                                  direction="column"
                                                  justifyContent="flex-start"
                                                  alignItems="flex-start"
                                             >
                                                  <Grid item width={'100%'}>
                                                       <Typography variant="body1" noWrap sx={{ fontSize: '20px' }}>Notebook name:</Typography>
                                                  </Grid>
                                                  <Grid item width={'100%'}>
                                                       <Typography variant="body2" noWrap sx={{ fontSize: '17px' }} color="text.secondary">{props.endpoint.notebookName}</Typography>
                                                  </Grid>
                                             </Grid>
                                        </Grid>
                                        <Grid item width={'50%'}>
                                             <Grid
                                                  container
                                                  direction="column"
                                                  justifyContent="flex-start"
                                                  alignItems="flex-start"
                                             >
                                                  <Grid item width={'100%'}>
                                                       <Typography variant="body1" noWrap sx={{ fontSize: '20px' }}>Function name:</Typography>
                                                  </Grid>
                                                  <Grid item width={'100%'}>
                                                       <Typography variant="body2" noWrap sx={{ fontSize: '17px' }} color="text.secondary">{props.endpoint.functionName}</Typography>
                                                  </Grid>
                                             </Grid>
                                        </Grid>
                                   </Grid>
                              </Grid>
                              <br />
                              <Grid item width={'100%'}>
                                   <Typography variant='body1' noWrap sx={{ fontSize: '20px' }}>Description of the endpoint:</Typography>
                              </Grid>
                              <Grid item width={'100%'}>
                                   <TextField
                                        disabled
                                        fullWidth
                                        variant="outlined"
                                        defaultValue={props.endpoint.description}
                                        sx={{ width: '100%' }}
                                   />
                              </Grid>
                         </Grid>
                    </CardContent>
               </Card>
               <br />
               <Card sx={{ maxWidth: '100%' }}>
                    <CardContent>
                         <Grid
                              container
                              direction="column"
                              justifyContent="space-around"
                              alignItems="flex-start"
                         >
                              <Grid item width={'100%'}>
                                   <Grid
                                        container
                                        direction="row"
                                        justifyContent="flex-start"
                                        alignItems="flex-start"
                                   >
                                        <Grid item width={'50%'}>
                                             <Grid
                                                  container
                                                  direction="column"
                                                  justifyContent="flex-start"
                                                  alignItems="flex-start"
                                             >
                                                  <Grid item width={'100%'}>
                                                       <InputLabel id="version-select-label">
                                                            <Typography variant='body1' noWrap sx={{ fontSize: '20px' }}>
                                                                 Version:
                                                            </Typography>
                                                       </InputLabel>
                                                  </Grid>
                                                  <Grid item width={'100%'}>
                                                       <Select
                                                            labelId="version-select-label"
                                                            id="version-select"
                                                            value={version}
                                                            onChange={handleVersionChange}
                                                            sx={{ width: 150 }}
                                                       >
                                                            {(versions.length > 0) ? (
                                                                 versions.map((ver) => (
                                                                      <MenuItem
                                                                           key={ver.id}
                                                                           value={ver.id}
                                                                      >
                                                                           <Grid
                                                                                container
                                                                                direction="row"
                                                                                justifyContent="space-between"
                                                                                alignItems="center"
                                                                           >
                                                                                <Grid item>{ver.versionName}</Grid>
                                                                                <Grid item><DeleteButton isSelected={version !== ver.id} versionId={ver.id} /></Grid>
                                                                           </Grid>
                                                                      </MenuItem>
                                                                 ))) : (
                                                                 <MenuItem key={0} value={0}>No version</MenuItem>
                                                            )}
                                                       </Select>
                                                  </Grid>
                                             </Grid>
                                        </Grid>
                                        <Grid item width={'50%'}>
                                             <Grid
                                                  container
                                                  direction="column"
                                                  justifyContent="space-between"
                                                  alignItems="flex-start"
                                             >
                                                  <Grid item width={'100%'}>

                                                       <InputLabel>
                                                            <Typography variant='body1' noWrap sx={{ fontSize: '20px' }}>
                                                                 Description:
                                                            </Typography>
                                                       </InputLabel>
                                                  </Grid>
                                                  <Grid item width={'100%'}>

                                                       <TextField
                                                            disabled
                                                            fullWidth
                                                            variant="standard"
                                                            InputProps={{
                                                                 disableUnderline: true,
                                                            }}
                                                            multiline
                                                            maxRows={2}
                                                            minRows={2}
                                                            value={versionDescription}
                                                            sx={{ width: '100%' }}
                                                       />
                                                  </Grid>
                                             </Grid>
                                        </Grid>
                                   </Grid>
                              </Grid>
                              <br />
                              <Grid item width={'100%'}>
                                   <InputLabel>
                                        <Typography variant='body1' noWrap sx={{ fontSize: '20px' }}>
                                             URL:
                                        </Typography>
                                   </InputLabel>
                                   <TextField
                                        disabled
                                        variant='outlined'
                                        value={endpointURLToCopy}
                                        sx={{ width: '100%' }}
                                        InputProps={{
                                             endAdornment: (
                                                  <AlignedInputAdornment position="end">
                                                       <Tooltip title="Copy Endpoint URL">
                                                            <IconButtonWithTooltip role={'button'} onClick={handleCopyToClipboard}>
                                                                 <IoCopyOutline />
                                                            </IconButtonWithTooltip>
                                                       </Tooltip>
                                                  </AlignedInputAdornment>
                                             ),
                                        }}
                                   />
                                   <Snackbar
                                        open={snackbarOpen}
                                        onClose={() => setSnackbarOpen(false)}
                                        autoHideDuration={2000}
                                        message="Copied to clipboard"
                                   />
                              </Grid>
                         </Grid>
                    </CardContent>
               </Card>
          </React.Fragment>
     )
};

export default EndpointSummary;
