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

namespace OPNsense\Noc\Api;

use OPNsense\Base\ApiControllerBase;
use OPNsense\Noc\Ezmesh;
use OPNsense\Core\Config;

/**
 * Class EzmeshController Handles Ezmesh related API actions for the Noc module
 * @package OPNsense\Noc
 */
class EzmeshController extends ApiControllerBase
{
    /**
     * retrieve ezmesh settings
     * @return array ezmesh settings
     * @throws \OPNsense\Base\ModelException
     * @throws \ReflectionException
     */
    public function getAction()
    {
        // define list of configurable settings
        $result = array();
        if ($this->request->isGet()) {
            $mdlEzmesh = new Ezmesh();
            $result['noc'] = $mdlEzmesh->getNodes();
        }
        return $result;
    }

    /**
     * update ezmesh settings
     * @return array status
     * @throws \OPNsense\Base\ModelException
     * @throws \ReflectionException
     */
    public function setAction()
    {
        $result = array("result" => "failed");
        if ($this->request->isPost()) {
            // load model and update with provided data
            $mdlEzmesh = new Ezmesh();
            $mdlEzmesh->setNodes($this->request->getPost("noc"));

            // perform validation
            $valMsgs = $mdlEzmesh->performValidation();
            foreach ($valMsgs as $field => $msg) {
                if (!array_key_exists("validations", $result)) {
                    $result["validations"] = array();
                }
                $result["validations"]["noc." . $msg->getField()] = $msg->getMessage();
            }

            // serialize model to config and save
            if ($valMsgs->count() == 0) {
                $mdlEzmesh->serializeToConfig();
                Config::getInstance()->save();
                $result["result"] = "saved!!!";
                $result["data"] = $this->request->getPost("noc");
            }
        }
        return $result;
    }
}
