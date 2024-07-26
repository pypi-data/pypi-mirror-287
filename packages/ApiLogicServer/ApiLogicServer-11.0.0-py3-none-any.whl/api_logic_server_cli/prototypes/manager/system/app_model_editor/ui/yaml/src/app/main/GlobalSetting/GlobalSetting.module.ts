import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {GLOBALSETTING_MODULE_DECLARATIONS, GlobalSettingRoutingModule} from  './GlobalSetting-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    GlobalSettingRoutingModule
  ],
  declarations: GLOBALSETTING_MODULE_DECLARATIONS,
  exports: GLOBALSETTING_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class GlobalSettingModule { }