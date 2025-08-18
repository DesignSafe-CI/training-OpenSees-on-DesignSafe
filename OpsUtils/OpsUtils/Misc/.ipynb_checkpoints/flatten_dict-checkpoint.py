def flatten_dict(d, parent_key='', sep='.'):
    """
    Recursively flattens a nested dictionary into a single-level dict
    with compound keys. Handles:

    - Nested dictionaries with keys joined by `sep`.
    - Lists, producing keys like `key[0]`, `key[1]`.
    - TapisResult objects by flattening their internal __dict__.
    - JSON strings that are actually dictionaries, continuing to flatten them.

    Useful for preparing complex Tapis job objects or deeply nested JSON
    for DataFrame creation, CSV export, or simplified logging.

    Parameters
    ----------
    d : dict
        The nested dictionary to flatten.

    parent_key : str, default=''
        Used internally to build up the compound keys.

    sep : str, default='.'
        Separator used to join keys.

    Returns
    -------
    dict
        A flattened dictionary with compound keys.

    Example
    -------
    flattened = flatten_dict(nested_dict)
    print(flattened['job.history[0].event'])  # → 'QUEUED'
    """
    # Silvia Mazzoni, 2025
    import json
    from tapipy.tapis import TapisResult
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if v is None or isinstance(v, (int, float)):
            items.append((new_key, v))
            continue
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
            continue
        if isinstance(v, list):
            for idx, item in enumerate(v):
                indexed_key = f"{new_key}[{idx}]"
                if isinstance(item, dict):
                    items.extend(flatten_dict(item, indexed_key, sep=sep).items())
                else:
                    items.append((indexed_key, item))
            continue
        if isinstance(v, TapisResult):
            items.extend(flatten_dict(v.__dict__, new_key, sep=sep).items())
            continue
        # Try to parse JSON strings that are dicts
        if isinstance(v, str):
            try:
                parsed_json = json.loads(v)
                if isinstance(parsed_json, dict):
                    items.extend(flatten_dict(parsed_json, new_key, sep=sep).items())
                    continue
            except (json.JSONDecodeError, TypeError):
                pass
        # Fallback: treat as plain value
        items.append((new_key, v))
    return dict(items)

