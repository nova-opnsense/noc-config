<?php

/**
 *   Copyright (c) 2021-2022 Nova Intelligent Technology JSC.,
 *   Author: hai.nt <hai.nt@novaintechs.com>
 *   
 *   All rights reserved.
 *   
 *   --------------------------------------------------------------------------------------
 *   
 *   
 */

namespace OPNsense\NOCConfig;

/**
 * Class EzmeshController
 * @package OPNsense\NOCConfig
 */
class EzmeshController extends \OPNsense\Base\IndexController
{
    public function indexAction()
    {
        // pick the template to serve to our users.
        $this->view->pick('OPNsense/NOCConfig/ezmesh');
        // fetch form data "ezmesh" in
        $this->view->ezmeshForm = $this->getForm("ezmesh");
    }
}
