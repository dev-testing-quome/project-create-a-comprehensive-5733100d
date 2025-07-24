// Primary UI Library: {ui_lib}
// Icons: {icons_lib}

// === CORE UI COMPONENTS ===
// shadcn/ui components
export { Button } from './ui/button';
export { Card, CardHeader, CardContent, CardFooter } from './ui/card';
export { Input } from './ui/input';
export { Label } from './ui/label';
export { Dialog, DialogContent, DialogHeader, DialogTitle, DialogTrigger } from './ui/dialog';
export { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from './ui/select';
export { Tabs, TabsContent, TabsList, TabsTrigger } from './ui/tabs';
export { Badge } from './ui/badge';
export { Alert, AlertDescription, AlertTitle } from './ui/alert';
export { Progress } from './ui/progress';

// === ICONS ===
export { 
  ChevronDown, ChevronRight, Check, X, Plus, Minus, Edit, Trash, 
  Search, Filter, Download, Upload, Settings, User, Home, Menu,
  ArrowLeft, ArrowRight, Calendar, Clock, Mail, Phone, Star,
  Heart, ShoppingCart, Eye, EyeOff, Lock, Unlock
} from 'lucide-react';

// === CUSTOM COMPONENTS ===
export { default as LoadingSpinner } from './custom/LoadingSpinner';
export { default as EmptyState } from './custom/EmptyState';
export { default as PageHeader } from './custom/PageHeader';
export { default as DataTable } from './custom/DataTable';
export { default as FormField } from './custom/FormField';

// === LAYOUT COMPONENTS ===
export { default as Layout } from './layout/Layout';
export { default as Sidebar } from './layout/Sidebar';
export { default as Header } from './layout/Header';
export { default as Footer } from './layout/Footer';

// === HOOKS ===
export { default as useLocalStorage } from '../hooks/useLocalStorage';
export { default as useDebounce } from '../hooks/useDebounce';
export { default as useApi } from '../hooks/useApi';
