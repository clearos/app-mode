<?php

/////////////////////////////////////////////////////////////////////////////
// General information
/////////////////////////////////////////////////////////////////////////////

$app['basename'] = 'mode';
$app['version'] = '1.0.10';
$app['release'] = '1';
$app['vendor'] = 'ClearFoundation';
$app['packager'] = 'ClearFoundation';
$app['license'] = 'GPLv3';
$app['license_core'] = 'LGPLv3';
$app['description'] = lang('mode_app_description');

/////////////////////////////////////////////////////////////////////////////
// App name and categories
/////////////////////////////////////////////////////////////////////////////

$app['name'] = lang('mode_app_name');
$app['category'] = lang('base_category_system');
$app['subcategory'] = lang('base_subcategory_settings');
$app['menu_enabled'] = FALSE;

/////////////////////////////////////////////////////////////////////////////
// Packaging
/////////////////////////////////////////////////////////////////////////////

$app['core_only'] = TRUE;

// Always pull in the simple mode driver for now.
$app['core_requires'] = array(
    'system-mode-driver',
    'app-simple-mode-core',
);

$app['core_file_manifest'] = array(
    'mode.conf' => array (
        'target' => '/var/clearos/mode',
        'mode' => '0600',
        'config' => TRUE,
        'config_params' => 'noreplace',
    ),
);

$app['core_directory_manifest'] = array(
   '/var/clearos/mode' => array(),
);
