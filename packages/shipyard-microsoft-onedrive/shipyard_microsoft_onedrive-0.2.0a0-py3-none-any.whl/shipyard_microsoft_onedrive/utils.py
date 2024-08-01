from shipyard_templates import ShipyardLogger, ExitCodeException, CloudStorage

logger = ShipyardLogger.get_logger()


def get_credential_group(args):
    if args.access_token:
        logger.debug("Using access token for authentication")
        return {"access_token": args.access_token}
    if args.client_id and args.client_secret and args.tenant:
        logger.debug("Using Client ID, Client Secret, and Tenant for authentication")
        return {
            "client_id": args.client_id,
            "client_secret": args.client_secret,
            "tenant": args.tenant,
        }
    raise ExitCodeException(
        "Either access token or Client ID, Client Secret, and Tenant must be provided",
        CloudStorage.EXIT_CODE_INVALID_INPUT,
    )
